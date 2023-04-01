#!/usr/bin/python3
#coding : utf-8

import os 

libs = {'pandas','numpy','openpyxl','penpyxl','urllib3','certifi','PyQt5','pyinstaller','pycparser'}

for lib in libs:
    os.system("pip install " + lib);