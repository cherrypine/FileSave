# Session2: StartBackPrograming
# Start office file back to the windows so that to get file path.
# FileType: .pptx .doc

import os
import FirstUse
import time

file = open(FirstUse.str_config + "\\config.txt","r",encoding="utf8")
path = file.read()
file.close()

paths = path.split("|")

os.system("start \"\" \"{}\"".format(paths[3]))
time.sleep(1)
os.system("start \"\" \"{}\"".format(paths[5]))
