#!/usr/bin/python3
# coding : utf-8


import pandas as pd
import csv

class readWrite:
    def readFile(file_name):
        result = pd.read_excel(file_name, sheet_name='Sheet1');
        return result;

    def writeFileCsv():
        with open("test.csv","w") as csvfile: 
            writer = csv.writer(csvfile);

            #先写入columns_name
            writer.writerow(["index","a_name","b_name"]);

            #写入多行用writerows
            writer.writerows([[0,1,3],[1,2,3],[2,3,4]]);


    def writeFileExcel():
        #创建一个空的Dataframe
        result =pd.DataFrame(columns=('idx','degree','weight','diameter'));
        #将计算结果逐行插入result,注意变量要用[]括起来,同时ignore_index=True，否则会报错，ValueError: If using all scalar values, you must pass an index
        idxs = [('12','45','0.6'),('13','47','0.9'),('14','56','1.0')]
        i = 1;
        for idx in idxs:
            degree = idx[0];
            weight =idx[1];
            diameter= idx[2];
            result = pd.concat([result, pd.DataFrame({'idx':[i],'degree':[degree],'weight':[weight],'diameter':[diameter]})],ignore_index=True);
            i= i+1;
        result.to_excel("test.xlsx", index=False);
        return 0;



if __name__ == "__main__":
    #readWrite.writeFileCsv();
    readWrite.writeFileExcel();
