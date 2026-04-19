from Tools.OSTool import getOS


# 创建文件夹
def create_folder(dir_path):
    import os
    # 判断文件夹是否存在
    if os.path.isdir(dir_path):
        return 0
    else:
        os.mkdir(dir_path)
        return 1


# 删除文件夹
def delete_folder(dir_path):
    import os
    # 判断是否为文件
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)  # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    # 判断是否为文件夹
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            # if file_name != 'wibot.log':
            tf = os.path.join(dir_path, file_name)
            # os.rmdir(tf)
            delete_folder(tf)
        print(dir_path)
        try:
            os.removedirs(dir_path)
        except FileNotFoundError:
            pass

    return True


import os

def open_folder(folder_path, use_app_path=True):
    """
    打开指定的文件夹。
    
    参数:
    folder_path (str): 文件夹路径。
    use_app_path (bool): 是否使用应用程序路径。
    """
    if not use_app_path:
        folder_path = os.path.join("..", folder_path)

    result = getOS()
    folder_path = os.path.abspath(folder_path)

    if result == 1:  # Linux系统
        os.system(f'xdg-open "{folder_path}"')
    elif result == 2:  # Windows系统
        folder_path = folder_path.replace("/", "\\")
        print(folder_path)
        os.system(f"explorer.exe {folder_path}")

if __name__ == '__main__':
    open_folder("test_pyml", True)
    path = "../Workbench/test_create"
    # create_folder(path)
    # os.removedirs(path)
    # delete_folder(path)
