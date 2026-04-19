# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: app.py
@time: 2020/6/9 上午8:47
"""
import os
import sys
import json
import multiprocessing
import requests
from requests import RequestException

from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename, send_from_directory

from Builder.CodeGenerator_Applications import json2applications_controller
from Builder.CodeGenerator_AutoML import json2AutoMLController
from Builder.CodeGenerator_Keras import json2kerasController
from Controller.Controller import ml_controller
from Database.GraphSQL import graph_save, graph_get, graph_delete
from Database.ProjectsSQL import project_list, project_create, chick_has_name, project_by_id, \
    project_update_update_time_by_id, project_get_path_by_id, project_delete, project_list_by_type, \
    project_list_by_name, project_get_name_by_id, project_list_by_name_and_type
from Database.Sqlite3Manager import longriver_history_select_all, \
    longriver_history_get_lasted_by_project_type_and_project_id
from Tools.CodeTools import cmdStarter, cmdLabelImgStarter, cmdStarterJupyterLab
from Tools.ExceptionHandler import exceptionHandler
from Tools.FileManeger import create_folder, open_folder, delete_folder
from Tools.JSONParser import get_node_by_id, get_node_by_pipeline_index
from Tools.PidManager import process_kill

app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False

global request_json
global global_pid


@app.route("/api/longriver/hello", methods=["GET", "POST"])
def flask_hello():
    """
    返回服务器的状态。

    请求方法:
    GET, POST

    返回:
    dict: 包含服务器状态的字典。
    """
    if request.method == "GET" or request.method == "POST":
        return {"status": "running"}


@app.route("/api/longriver/login", methods=["POST"])
def login():
    """
    用户登录。

    请求方法:
    POST

    请求参数:
    name (str): 用户名。
    password (str): 密码。

    返回:
    dict: 用户登录状态。
    """
    from Database.UserSQL import user_login
    return user_login(request.json["name"], request.json["password"])
    # return 'login page'
    # 暂时没有跳转


@app.route("/api/longriver/kill", methods=["GET", "POST"])
def flask_stop_keras_process():
    """
    停止正在运行的程序
    程序指单独运行的生成的代码，
    服务器默认以多线程模式运行，
    因此需要global_pid杀死。

    请求方法:
    GET, POST

    返回:
    dict: 包含进程状态和错误信息的字典。
    """
    if not globals().get('global_pid'):
        return {"keep_running": "True", "kill_process": "False", "pid": "None", "error": "global_pid is not defined"}
    try:
    # redis
    # pid_killer(request_json)  # 修改redis状态
        pass
    except Exception as e:
        return {"kill": "False", "pid": "None", "error": str(e)}

    if request.method == "GET" or request.method == "POST":
        kill = False
        while not kill:
            kill = process_kill(global_pid)
        return {"kill": str(kill), "pid": global_pid}


def flask_stop_global_pid():
    """
    停止全局进程 ID。

    返回:
    dict: 包含进程状态和错误信息的字典。
    """
    if not globals().get('global_pid'):
        return {"keep_running": "True", "kill_process": "False", "pid": "None", "error": "global_pid is not defined"}
    
    kill_process = False
    while not kill_process:
        kill_process = process_kill(global_pid)
    
    return {"keep_running": str(kill_process), "kill_process": kill_process, "pid": global_pid}


@app.route("/api/longriver/automl", methods=["GET", "POST"])
def flask_json_to_automl():
    # 定义一个路由，用于将json数据转换为AutoML
    result_stop_global_pid = flask_stop_global_pid()
    if result_stop_global_pid["keep_running"] == "False":
        result_stop_global_pid["kill"] = result_stop_global_pid["kill_process"]
        return {"status": "中断程序异常", "error": "平台发送了中断原运行程序的命令，但该命令未得到正确的执行结果"}

    global request_json
    request_json = request.json.copy()
    project_name = project_get_name_by_id(request.json["project_id"])
    request_json = request_json['countJson']

    global global_pid
    bl_run_generate_code = bool(int(get_node_by_pipeline_index(request_json, "-1")["params"]["bl_run_generate_code"]))

    if request.method == "GET" or request.method == "POST":
        p = multiprocessing.Process(
            target=json2AutoMLController, args=(
                project_name, request_json, bl_run_generate_code))
        p.start()
        global_pid = p.pid
        return {"status": "multiprocessing ok", "pid": global_pid}


@app.route("/api/longriver/applications", methods=["GET", "POST"])
def flask_json_to_applications():
    # 定义一个路由，用于将json数据转换为Applications
    result_stop_global_pid = flask_stop_global_pid()
    if result_stop_global_pid["keep_running"] == "False":
        result_stop_global_pid["kill"] = result_stop_global_pid["kill_process"]
        return {"status": "中断程序异常", "error": "平台发送了中断原运行程序的命令，但该命令未得到正确的执行结果"}

    global request_json
    request_json = request.json.copy()
    project_name = project_get_name_by_id(request.json["project_id"])
    request_json = request_json['countJson']
    bl_run_generate_code = bool(int(get_node_by_pipeline_index(request_json, "-1")["params"]["bl_run_generate_code"]))
    global global_pid

    if request.method == "GET" or request.method == "POST":
        p = multiprocessing.Process(
            target=json2applications_controller, args=(project_name, request_json, bl_run_generate_code)
        )
        p.start()
        global_pid = p.pid
        return {"status": "multiprocessing ok", "pid": global_pid}


@app.route("/api/longriver/keras", methods=["GET", "POST"])
def flask_json_to_keras():
    # 定义一个路由，用于将json数据转换为Keras
    result_stop_global_pid = flask_stop_global_pid()
    if result_stop_global_pid["keep_running"] == "False":
        result_stop_global_pid["kill"] = result_stop_global_pid["kill_process"]
        return {"status": "中断程序异常", "error": "平台发送了中断原运行程序的命令，但该命令未得到正确的执行结果"}

    global request_json
    request_json = request.json.copy()
    request_json = request_json['countJson']
    project_name = project_get_name_by_id(request.json["project_id"])

    bl_run_generate_code = 1
    try:
        bl_run_generate_code = bool(
            int(get_node_by_pipeline_index(request_json, "-1")["params"]["bl_run_generate_code"]))
    except KeyError:
        print("参数获取异常：", str(KeyError))
    global global_pid

    if request.method == "GET" or request.method == "POST":
        p = multiprocessing.Process(
            target=json2kerasController, args=(project_name, request_json, bl_run_generate_code))
        p.start()
        global_pid = p.pid
        return {"status": "multiprocessing ok", "pid": global_pid}


@app.route("/api/longriver/pyml", methods=["GET", "POST"])
def flask_json_to_pyml():
    # 定义一个路由，用于将json数据转换为PyML
    result_stop_global_pid = flask_stop_global_pid()
    if result_stop_global_pid["keep_running"] == "False":
        result_stop_global_pid["kill"] = result_stop_global_pid["kill_process"]
        return {"status": "中断程序异常", "error": "平台发送了中断原运行程序的命令，但该命令未得到正确的执行结果"}

    global request_json
    request_json = request.json.copy()

    # 040 暂不开放该功能
    # 保存计算图到历史记录表
    # longriver_history_insert(request_json['project_id'], request_json['countJson'], request_json['project_type'])
    request_json = request_json['countJson']
    project_name = project_get_name_by_id(request.json["project_id"])

    global global_pid
    # 判断是否运行，0表示不运行生成代码，1表示运行生成代码
    bl_run_generate_code = bool(int((get_node_by_id(request_json, "-1")["bl_run_generate_code"])))
    # 获取配置信息，id、index均为0
    # node = get_node_by_id(request_json, "0")

    # str_redis = "redis"
    # 使用异步线程执行具体代码生成与调用任务
    if request.method == "GET" or request.method == "POST":
        p = multiprocessing.Process(
            target=ml_controller, args=(project_name, request_json, None, bl_run_generate_code)
        )
        p.start()
        global_pid = p.pid
        return {"status": "multiprocessing ok", "pid": global_pid}


@app.route("/api/longriver/code", methods=["GET", "POST"])
def code():
    # 定义一个路由，用于生成代码
    has_file = False
    file_name = ""
    for i in [
        "generate_code_applications.py",
        "generate_code_keras.py",
        "generate_code_pyml.py",
        "generate_code_paddle.py",
        "generate_code_automl.py",
    ]:
        if os.path.exists(i):
            file_name = i
            has_file = True
    if not has_file:
        return {"status": "no file"}

    with open(file_name, "r") as f:
        file_list = f.read().split("\n")

    file_clean_list = []
    for i in file_list:
        if i != "import redis" and i.lstrip()[0:4] not in [
            "pool",
            "redi",
            "prin",
            "exce",
            "try:",
            "def ",
        ]:
            file_clean_list.append(i.replace("        ", ""))

    from Tools import work_path

    code_file_path = (work_path + "/code_automatically_generated_by_longriver.py").replace("//", "/")
    f = open(code_file_path, "w")
    f.truncate()
    for i in file_clean_list:
        f.writelines(i + "\n")
    f.close()
    os.system(
        "autopep8 --in-place --aggressive --aggressive " +
        code_file_path)
    os.system("black " + code_file_path)
    os.system("cp -r DataReader/ " + work_path)

    return {"status": "end"}


@app.route("/")
def home():
    # 定义一个路由，用于返回主页
    return render_template("index.html")


@app.route("/api/longriver/readme")
def readme():
    # 定义一个路由，用于返回README文件
    return render_template("README.html")


@app.route("/api/longriver/status", methods=["GET", "POST"])
def status():
    # 定义一个路由，用于返回服务器的状态
    return {}


# # 设置文件上传保存路径
# app.config['UPLOAD_FOLDER'] = 'static/upload/'
# # MAX_CONTENT_LENGTH设置上传文件的大小，单位字节
# app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


# 下载
@app.route('/api/longriver/download/<filename>', methods=['GET'])
def download(filename):
    # 定义一个路由，用于下载文件
    from Tools import work_path
    if request.method == "GET":
        # 通过文件名下载文件
        path = os.path.isfile(os.path.join(work_path, filename))
        if path:
            return send_from_directory(work_path, filename, as_attachment=True)


# 模型覆盖上传
@app.route('/mode/upload', methods=['POST'])
def mode_upload():
    # 定义一个路由，用于上传模型
    try:
        file = request.files['model']
        file_path = "./ModelLibrary/" + secure_filename(file.filename)
        if os.path.exists(file_path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(file_path)
        file.save(file_path)
        return jsonify({"status": "successful", "content": "File upload successful", "function": "mode_upload"}), 200
    except Exception as err:
        list_tmp = exceptionHandler(err)
        return jsonify(list_tmp[0]), list_tmp[1]


# 模型下载
@app.route('/mode/download/<modelname>', methods=['GET'])
def mode_download(modelname):
    # 定义一个路由，用于下载模型
    try:
        if request.method == "GET":
            # 通过文件名下载文件
            from Tools import work_path
            model_path = os.path.join(work_path, "ModelLibrary", secure_filename(modelname))
            if os.path.isfile(model_path):
                return send_from_directory(os.path.dirname(model_path), os.path.basename(model_path), as_attachment=True)

    except Exception as err:
        list_tmp = exceptionHandler(err)
        return jsonify(list_tmp[0]), list_tmp[1]


@app.route('/api/longriver/project/create', methods=['POST'])
def post_project_create_by_id():
    # 定义一个路由，用于创建项目
    if chick_has_name(request.json["name"]):
        return {"status": "项目名称已存在"}

    from Tools import work_path
    is_create_folder = create_folder(work_path + request.json["name"])
    if is_create_folder == 0:
        return {"status": "同名文件夹已存在，创建项目文件夹失败"}

    project_create(request.json["name"], request.json["user_id"], work_path + request.json["name"], request.json["type"])
    return {"status": "创建项目与项目文件夹成功"}


@app.route('/api/longriver/project/delete', methods=['DELETE'])
def project_delete_by_id():
    """
    根据项目 ID 删除项目。

    参数:
    project_id (str): 项目 ID。

    返回:
    dict: 包含删除状态和错误信息的字典。
    """
    project_id = request.json.get("project_id")
    if not project_id:
        return {"status": "error", "message": "项目 ID 未提供"}

    try:
        path = project_get_path_by_id(request.json["project_id"])
        if path is None or path.replace(" ", "") == "":
            return {"status": "error", "message": "项目未找到"}

        path = './' + path + '/'
        delete_folder(path)
        project_delete(request.json["project_id"], request.json["user_id"])
        graph_delete(request.json["project_id"], request.json["user_id"])
        return {"status": "success", "message": "项目已成功删除"}

    except Exception as err:
        print(err)
        # return {"status": "代码执行失败，请手动检查文件夹与数据库数据是否删除成功", "error": err}
        return {"status": "error", "message": f"删除项目时出错: {str(err)}"}



@app.route('/api/longriver/project/list', methods=['GET'])
def get_project_list():
    # 定义一个路由，用于获取项目列表
    header, data = project_list()
    return jsonify({"header": header, "data": data})


@app.route('/api/longriver/project/data', methods=['GET'])
def get_project_by_id():
    # 定义一个路由，用于获取项目信息
    header, data = project_by_id(request.json["user_id"], request.json["project_id"])
    # if not result:
    #     return {"status": "未查询有效信息"}
    return jsonify({"header": header, "data": data})


@app.route('/api/longriver/project/list/by-type', methods=['GET'])
def get_project_list_by_type():
    # 定义一个路由，用于根据类型获取项目列表
    header, data = project_list_by_type(request.json["user_id"], request.json["type"])
    # if not result:
    #     return {"status": "未查询有效信息"}
    return jsonify({"header": header, "data": data})


@app.route('/api/longriver/project/list/by-name', methods=['GET'])
def get_project_list_by_name():
    # 定义一个路由，用于根据名称获取项目列表
    header, data = project_list_by_name(request.json["user_id"], request.json["name"])
    # if not result:
    #     return {"status": "未查询有效信息"}
    return jsonify({"header": header, "data": data})


@app.route('/api/longriver/project/list/by-name-type', methods=['GET', 'POST'])
def get_project_list_by_name_and_type():
    # 定义一个路由，用于根据名称和类型获取项目列表
    if request.json.get("user_id"):
        if request.json.get("name") and request.json.get("type"):
            header, data = project_list_by_name_and_type(request.json.copy())
        elif request.json.get("name"):
            header, data = project_list_by_name(request.json["user_id"], request.json["name"])
        elif request.json.get("type"):
            header, data = project_list_by_type(request.json["user_id"], request.json["type"])
        else:
            return {"status": "无法根据输入的筛选条件查询到有效信息"}, 404
        return jsonify({"header": header, "data": data})
    else:
        return {"status": "未能获得有效的用户id"}, 401


@app.route('/api/longriver/project/listdir', methods=['GET'])
def project_listdir():
    # 定义一个路由，用于获取项目文件夹列表
    from Tools import work_path

    path = work_path + request.json["project_name"] + '/'
    listdir = [f for f in os.listdir(path)]
    print(jsonify(listdir))
    return jsonify(listdir), 200


@app.route('/api/longriver/graph/save/', methods=['POST'])
def post_graph_save():
    # 定义一个路由，用于保存计算图
    result = graph_save(request.json["project_id"], request.json["user_id"], request.json["graph"])
    project_update_update_time_by_id(request.json["project_id"])
    if result:
        return {"status": "保存成功"}
    else:
        return {"status": "创建失败"}


@app.route('/api/longriver/graph/get', methods=['GET', 'POST'])
def post_graph_get():
    # 定义一个路由，用于获取计算图
    header, data = graph_get(request.json["project_id"], request.json["user_id"])
    project_update_update_time_by_id(request.json["project_id"])
    return jsonify({"header": header, "data": data})


@app.route('/files/listdir/<path>', methods=['GET'])
def files_path(project_name):
    # 定义一个路由，用于获取文件列表
    path = 'projects/' + project_name.replace("_", "/") + '/'
    listdir = [f for f in os.listdir(path)]
    print(listdir)
    return jsonify(listdir), 200


@app.route('/api/longriver/files/open-window', methods=['POST'])
def files_open_window():
    # 定义一个路由，用于打开文件窗口
    try:
        str_path = project_get_path_by_id(request.json['project_id'])
        open_folder(str_path)
        return {"status": "代码执行完成，请查看窗口是否打开"}
    except Exception as err:
        return {"status": "代码执行失败，请手动查看窗口是否打开", "error": str(err)}


@app.route('/api/longriver/history/list', methods=['GET'])
def history_list():
    result = longriver_history_select_all()
    if not result:
        return None
    else:
        return jsonify(result)


@app.route('/api/longriver/history/cancel', methods=['POST'])
def history_cancel():
    print(request_json)
    result = longriver_history_get_lasted_by_project_type_and_project_id(request.json['project_id'],
                                                                         request.json['project_type'])

    print(result)
    if not result:
        return None
    else:
        return jsonify(result)


@app.route('/api/chartGPT/llama/v31/forward', methods=['POST', 'GET'])
def forward_request(model_url="http://localhost", port="11434"):
    # http://localhost:11434/
    try:
        url = "http://localhost:11434/api/generate"

        import json
        # print("json : " + json.dumps(str(request.json.copy())))
        # payload = json.dumps(str(request.json.copy()))

        # print("JSON : " + request.json)
        print("prompt : " + request.json['prompt'])

        payload = json.dumps({
            "model": "llama3.1",
            # "prompt": "帮我写一个js函数，获取当前的时间，格式为xxx年xx月xx日 xx：xx：xx",
            "prompt": request.json['prompt'],
            "stream": False
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload, timeout=100)
        print(response.text)

        return response.text
    except RequestException as e:
        print(f'RequestException: {e}')
        print(f'RequestException__context__: {e.__context__}')
        # 在这里可以添加错误处理逻辑
    except ValueError as e:
        print(f'ValueError: {e}')
        # 在这里可以添加错误处理逻辑


@app.route('/api/longriver/codetools/jupyter/notebook', methods=['POST', 'GET'])
def codetools_jupyter_notebook():
    # 要执行的命令
    command = "jupyter notebook"  # 在Linux或macOS上启动 jupyter notebook
    # command = "%tensorboard --logdir logs"  # 在Linux或macOS上列出当前目录的文件

    # 启动独立线程执行终端命令，避免线程堵塞
    # 使用multiprocessing + subprocess.run执行命令
    p = multiprocessing.Process(target=cmdStarter)
    p.start()
    return {"status": "Successful", "content": "执行完成，请查看jupyter的浏览器窗口是否打开，首个服务默认端口为8888"}


@app.route('/api/longriver/codetools/jupyter/lab', methods=['POST', 'GET'])
def codetools_jupyter_lab():
    # 要执行的命令
    command = "jupyter notebook"  # 在Linux或macOS上启动 jupyter notebook
    # command = "%tensorboard --logdir logs"  # 在Linux或macOS上列出当前目录的文件

    # 启动独立线程执行终端命令，避免线程堵塞
    # 使用multiprocessing + subprocess.run执行命令
    p = multiprocessing.Process(target=cmdStarterJupyterLab)
    p.start()
    return {"status": "Successful", "content": "执行完成，请查看jupyter lab的浏览器窗口是否打开，首个服务默认端口为8888"}


@app.route('/api/longriver/codetools/labelImg', methods=['POST', 'GET'])
def codetools_labelImg():
    # 要执行的命令
    # command = "labelImg"  # 在Linux或macOS上启动 jupyter notebook

    # 启动独立线程执行终端命令，避免线程堵塞
    # 使用multiprocessing + subprocess.run执行命令
    p = multiprocessing.Process(target=cmdLabelImgStarter)
    p.start()

    return {"status": "Successful", "content": "代码执行完成，请检查数据标注工具labelImg窗口是否打开"}


if __name__ == "__main__":
    """
    启动 Flask 应用程序。
    """
    # 生产环境应该使用 WSGI 服务器，如 Gunicorn 或 uWSGI
    # 本地开发时可以使用内置服务器
    
    # 生产环境配置（推荐）
    # from gevent import pywsgi
    # server = pywsgi.WSGIServer(("0.0.0.0", 9703), app)
    # server.serve_forever()
    
    # 开发环境配置
    import logging
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=9703, debug=False, threaded=True)
