import os

for root,dirs ,files in os.walk(r"D:\MyPython\DetectionSystem\tmp\readpdf\pdf"):
    for file in files:
        print(os.path.join(root,file))
