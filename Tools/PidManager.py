# encoding: utf-8

def process_kill(pid):
    import psutil
    import time

    try:
        p = psutil.Process(pid)
        p.kill()
        time.sleep(0.001)
    except psutil.NoSuchProcess:
        return True
    if p.status() == "zombie" or p.status() == "dead":
        return True
    else:
        return False
