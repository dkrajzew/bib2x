



# --- imports ---------------------------------------------------------------
import os
import shutil
TEST_PATH = os.path.split(__file__)[0]



# --- helper functions ----------------------------------------------
def pname(string, name, path="<DIR>"):
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", name).replace("pytest", name).replace("optional arguments", "options")


def text_read(path):
    with open(path, "r") as fd:
        return fd.read()


def copy_files(tmp_path, files):
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), file), str(tmp_path / file))

