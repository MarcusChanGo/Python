#!/usr/bin/python3
# coding: utf-8

import pandas as pd

class readWriteFile:
    def readFile():
        print("begin read!!");
        result = pd.read_excel('./Book1.xlsx',sheet_name='Sheet1');
        return result;
    
    def writeFile():
        writer=pd.ExcelWriter('\\sale_january_2017_in_pandas.xlsx');
        writer.save();
        return