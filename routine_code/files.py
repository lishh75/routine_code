import os
def files(path):
    files=os.listdir(path)
    for i in files:
        print(i)