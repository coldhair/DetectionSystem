import os
path=r'D:\MyPython\DetectionSystem\tmp\float.html'

base_name=os.path.basename(path)
print(base_name)
dir_name=os.path.dirname(path)
print(dir_name)
join_path=os.path.join('temp','data',os.path.basename(path))
print(join_path)
print(os.path.split(path))
