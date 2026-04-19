import sqlite3


def graph_save(project_id, user_id, graph, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')

    r = connect.execute("DELETE FROM graph where project_id=" + str(project_id) + " and user_id =" + str(user_id))
    r = connect.executemany("INSERT INTO graph(project_id, user_id, graph) VALUES(?,?,?);",
                            [[project_id, user_id, graph]])
    r = r.fetchall()
    connect.commit()
    connect.close()
    return True


def graph_delete(project_id, user_id, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')

    r = connect.execute("DELETE FROM graph where project_id=" + str(project_id) + " and user_id =" + str(user_id))

    connect.commit()
    connect.close()
    return True


def graph_get(project_id, user_id, ues_app_path=True):
    if ues_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')
    r = connect.execute(
        "SELECT id,user_id,project_id,graph FROM graph where user_id=" + str(user_id) + " and project_id =" + str(
            project_id) + ";")

    r = r.fetchall()
    connect.commit()
    connect.close()
    return ["id", "user_id", "project_id", "graph"], r


if __name__ == '__main__':
    result = graph_save(1, 1, "update123", False)
    print(result)
