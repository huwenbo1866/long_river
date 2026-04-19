import subprocess


def cmdStarter(command="jupyter notebook"):
    # 要执行的命令
    # command = "jupyter notebook"  # 在Linux或macOS上启动 jupyter notebook
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    # 输出执行结果
    print("命令输出:\n", result.stdout)

    # 检查是否有错误输出
    if result.stderr:
        print("命令错误:\n", result.stderr)


def cmdStarterJupyterLab(command="jupyter lab"):
    # command = "jupyter notebook"  # 在Linux或macOS上启动 jupyter notebook
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    # 输出执行结果
    print("命令输出:\n", result.stdout)

    # 检查是否有错误输出
    if result.stderr:
        print("命令错误:\n", result.stderr)


def cmdLabelImgStarter(command="labelImg"):
    # command = "jupyter notebook"  # 在Linux或macOS上启动 jupyter notebook
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    # 输出执行结果
    print("命令输出:\n", result.stdout)

    # 检查是否有错误输出
    if result.stderr:
        print("命令错误:\n", result.stderr)
