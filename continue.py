import shutil
import os
import tkinter
from tkinter import filedialog
file=filedialog.askdirectory()
with open("log.txt","w") as doc:
    pass
os.chdir(file)
files=os.listdir(file)
begin=int(input("rename to:"))
s=sorted(files,lambda x: os.path.getctime(os.path.join,x))
for elt in files:
    if not os.path.isdir(elt):
        dump=elt.split("/")[-1]+"-------------->"+str(begin)+"\n"
        with open("log.txt","a") as doc:
            doc.write(dump)
        os.rename(elt,str(begin)+".ts")
        begin+=1
    elif elt=="log.txt":
        pass