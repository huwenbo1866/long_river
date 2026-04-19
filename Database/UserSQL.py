import sqlite3  # 驱动


def user_login(user_name, user_pwd, use_app_path=True):
    if use_app_path:
        connect = sqlite3.connect('resources/longriver.db')
    else:
        connect = sqlite3.connect('../resources/longriver.db')

    # r = connect.execute("SELECT * FROM history limit " + limit)
    r = connect.execute("SELECT id,name,password,level FROM user where is_deleted==0")
    # 获取查询结果
    r = r.fetchall()
    for i in r:
        if i[1] == user_name:
            if i[2] == user_pwd:
                connect.commit()
                connect.close()
                return {"status": "登陆成功"}
            else:
                connect.commit()
                connect.close()
                return {"status": "密码错误"}
        else:
            connect.commit()
            connect.close()
            return {"status": "未查询到本用户"}


if __name__ == '__main__':
    result = user_login("root", "root", False)
    print(result)
