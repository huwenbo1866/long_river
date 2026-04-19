import platform


def getOS():
    os_name = platform.system()
    if os_name == 'Linux':
        return 1
    elif os_name == 'Windows':
        return 2
    else:
        return 0
