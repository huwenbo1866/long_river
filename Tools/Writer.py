# encoding: utf-8
from Tools.OSTool import getOS


def cw_str(string):
    return '"' + string + '"'


def end_of_line_character_handling(string):
    if string[-1] == "(":
        string += ")"
    elif string[-1] == ",":
        string = string[:-1] + ")"
    elif string[-2] == ",":
        string = string[:-2] + ")"
    else:
        pass
    return string


# 040
def code_writer(file_path, list_code_before, msg):
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.writelines("# encoding: utf-8\n")
        for item in list_code_before:
            f.writelines(item.replace("//", "/") + "\n")

        f.writelines("\ndef generator_code():\n")

        for item in msg:
            f.writelines("    " + item.replace("//", "/") + "\n")


def code_clear_writer(project_name, file_name="auto", writer_file_name="keras"):
    import os

    if file_name == "auto":
        for i in [
            "generate_code_applications.py",
            "generate_code_keras.py",
            "generate_code_pyml.py",
            "generate_code_paddle.py",
            "generate_code_automl.py",
        ]:
            if os.path.exists(i):
                file_name = "../" + i
    else:
        file_name = "generate_code_" + file_name + ".py"

    if not os.path.exists(file_name):
        return {"status": "no file"}

    with open(file_name, "r", encoding="utf-8") as f:
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
            if i != "":
                if i[0:12] == "            ":
                    file_clean_list.append(i.replace("            ", "    "))
                elif i.startswith("        model"):
                    file_clean_list.append(i.replace("        ", "    "))
                else:
                    file_clean_list.append(i.replace("    ", ""))

    from Tools import work_path

    work_path_with_project = "" + str(work_path) + "/" + str(project_name) + "/"
    code_file_path = (
            work_path_with_project
            + "/automatically_generated_code_by_longriver_for_"
            + writer_file_name
            + ".py"
    ).replace("//", "/")
    with open(code_file_path, "w", encoding="utf-8", newline="\n") as f:
        for i in file_clean_list:
            i = i.replace('Workbench/', "./")
            if i is not None and i.strip() != "":
                f.writelines(i + "\n")
            else:
                f.writelines("\n")
    # os.system("black " + code_file_path)
    os_type = getOS()
    if os_type == 1:
        os.system("cp -r ./DataReader/ " + work_path_with_project)
        if file_name == "applications":
            os.system("cp -r ./algorithmlib/ " + work_path_with_project)
    if os_type == 2:
        import shutil
        shutil.copytree(str(os.getcwd() + "/DataReader").replace("/", "\\"),
                        str(work_path_with_project + "/DataReader").replace("/", "\\"), dirs_exist_ok=True)
        if file_name == "applications":
            shutil.copytree(str(os.getcwd() + "/algorithmlib").replace("/", "\\"),
                            str(work_path_with_project + "/algorithmlib").replace("/", "\\"), dirs_exist_ok=True)
    return {"status": "ok"}
