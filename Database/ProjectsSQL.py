import sqlite3


def project_list(use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT id,name,owner_id,path,type,create_time,update_time FROM projects;")
    # 获取查询结果
    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "name", "owner_id", "path", "type", "create_time", "update_time"], r


def project_by_id(user_id, project_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT id,name,owner_id,path,type,create_time,update_time FROM projects where owner_id=" + str(
        user_id) + " and id =" + str(project_id) + ";")
    # 获取查询结果
    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "name", "owner_id", "path", "type", "create_time", "update_time"], r


def project_list_by_type(user_id, project_type, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT id,name,owner_id,path,type,create_time,update_time FROM projects where owner_id=" + str(
        user_id) + " and type =" + str(project_type) + ";")
    # 获取查询结果
    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "name", "owner_id", "path", "type", "create_time", "update_time"], r


def project_list_by_name(user_id, project_name, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT id,name,owner_id,path,type,create_time,update_time FROM projects where owner_id=" + str(
        user_id) + " and name LIKE \"" + str(project_name) + "%\";")
    # 获取查询结果
    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "name", "owner_id", "path", "type", "create_time", "update_time"], r


def project_list_by_name_and_type(request_json, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')

    r = connect.execute("SELECT id,name,owner_id,path,type,create_time,update_time FROM projects where owner_id=" + str(
        request_json['user_id']) + " and name LIKE \"" + str(request_json['name']) + "%\" and type =" + str(
        request_json['type']) + ";")

    # 获取查询结果
    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "name", "owner_id", "path", "type", "create_time", "update_time"], r


def project_create(name, owner_id, path, project_type, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    import time
    create_time = time.time()
    connect.executemany(
        "INSERT INTO projects(name, owner_id, path, create_time, type, update_time) VALUES(?,?,?,?,?,?);",
        [[name, owner_id, path, create_time, project_type, create_time]])
    connect.commit()
    connect.close()


def chick_has_name(name, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT id FROM projects where name=\"" + str(name) + "\"")
    r = r.fetchall()
    connect.commit()
    connect.close()
    if not r:
        return False
    else:
        return True


def project_update_update_time_by_id(project_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    import time
    update_time = time.time()
    connect.execute("UPDATE projects set update_time = \"" + str(update_time) + "\" where ID=" + str(project_id))
    connect.commit()
    connect.close()


def project_delete_by_id(project_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("DELETE FROM projects where id=" + str(project_id) + "")
    r = r.fetchall()
    connect.commit()
    connect.close()
    if not r:
        return False
    else:
        return True


def project_get_path_by_id(project_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT path FROM projects where id=\"" + str(project_id) + "\"")
    r = r.fetchall()
    connect.commit()
    connect.close()
    if not r:
        return None
    else:
        return r[0][0]


def project_get_name_by_id(project_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("SELECT name FROM projects where id=\"" + str(project_id) + "\"")
    r = r.fetchall()
    connect.commit()
    connect.close()
    if not r:
        return None
    else:
        return r[0][0]


def project_delete(project_id, user_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute("DELETE FROM projects where id=" + str(project_id) + " and owner_id =" + str(user_id))
    connect.commit()
    connect.close()


if __name__ == '__main__':
    # project_get_path_by_id(1, False)
    # project_delete(7, 1, False)
    print(project_list_by_name(1, "dm", use_app_path=False))
