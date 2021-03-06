from importlib.resources import path
import sys
import os
import shutil
from git import Repo
from subprocess import call
from git import RemoteProgress
from tqdm import tqdm


version = "0.1"
paths = os.getenv('APPDATA')
mcpath = ("\.minecraft\mods")
pathstring = str(paths + mcpath)

print("modinstaller", version)
os.chdir (pathstring)
print ("removing .git folder")
os.system ("rmdir /S .git")
print("WARNING mods folder is about top be completely wiped")
safety = input("exit this window to cancel mod deletion or press enter to continue")
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

class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

Repo.clone_from(gitaddress, pathstring, branch='main', progress=CloneProgress())