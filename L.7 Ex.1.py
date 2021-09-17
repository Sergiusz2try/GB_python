import os
import shutil

ROOT = './'
dirs_names = ['settings', 'mainapp', 'adminapp', 'authapp']

for el in dirs_names:
    dir_name = 'my_project'
    dirs_path = f'{dir_name}/{el}'
    dir_path = os.path.join(ROOT, dirs_path)
    if not os.path.exists(dir_path):
        os.makedirs(dirs_path)
    else:
        shutil.rmtree(dir_path)
