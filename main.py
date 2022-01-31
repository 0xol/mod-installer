from importlib.resources import path
import sys
import os
import shutil
from git import Repo

version = "0.1"
paths = os.getenv('APPDATA')
mcpath = ("\.minecraft\mods")
pathstring = str(paths + mcpath)

print("modinstaller", version)
os.chdir (pathstring)

folder = pathstring
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
    
gitaddress = input("enter git address: ")


Repo.clone_from(gitaddress, pathstring)