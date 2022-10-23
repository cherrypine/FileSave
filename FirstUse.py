# Session1: FirstUse
# When you first use this programing or start windows it will be ran.

import os
import tkinter.messagebox as message # Popup
import tkinter.filedialog as filec   # Choose file path

str_cwd = os.getcwd()                # Get working path
str_config = str_cwd + "\\config"    # Get config path

# To configure the program
if not os.path.exists(str_config):
    os.mkdir(str_config)
    message.showinfo("FastTool", "Choose a file path to save your file. (1/3)")
    filepath = filec.askdirectory()
    message.showinfo("FastTool", "Choose a floder which is installed Powerpoint. (2/3)")
    pptpath = filec.askopenfilename()
    message.showinfo("FastTool", "Choose a floder which is installed Word. (3/3)")
    wordpath = filec.askopenfilename()
    message.showinfo("FastTool", "Now: Runing")
    
    # 指定编码方式为 utf8
    file = open(str_config + "\\config.txt","w",encoding="utf8")

    # write方法会将字符串编码为utf8字节串写入文件
    file.write("LessonResources|" + filepath + "|" +
            "Powerpoint|" + pptpath + "|" +
            "Word|" + wordpath)

    # 文件操作完毕后， 使用close 方法关闭该文件对象
    file.close()