import os, shutil, time

path = r"C:\Users\bisterj\Downloads"

while True:
    files = os.listdir(path)

    for file in files:
        if os.path.isfile(path + "\\" + file):
            ext = file.split('.')[-1]
            if not os.path.exists(path + "\\" + ext + " files"): 
                os.mkdir(path + "\\" + ext + " files")
            os.rename(path + "\\" + file, path + "\\" + ext + " files" + "\\" + file)

    time.sleep(300)