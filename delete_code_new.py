#!/bin/env python
# --*--coding:utf-8 --*--
# author:chenxm


import os
import re
import sys
import time
import difflib
import argparse
import cchardet
import progressbar
import pyprind
from tqdm import tqdm 
from bs4 import BeautifulSoup


def get_coding(file):
    with open(file, "rb") as fp:
        return cchardet.detect(fp.read())["encoding"]


# write file 
def write_file(file, content):
    result_file = open(file, 'a+', encoding="utf-8")
    result_file.write(content + "\n")
    result_file.close()


#analyze file and output result
def rewrite_code(file, lhead, rhead, thead):
    lflag = 0
    rflag = 0
    url = "Report.html"

    #Judge the encoding of Roport.html
    encode = get_coding(url)
    if(encode == "GB2312" or encode == "GB18030"):
        soup = BeautifulSoup(open(url, 'r'), "html.parser")
    elif(encode == "UTF-8"):
        soup = BeautifulSoup(open(url, 'r',encoding='utf-8'), "html.parser")
    elif(encode == "UTF-8-SIG"):
        soup = BeautifulSoup(open(url, 'r',encoding='utf-8-sig'), "html.parser")
    else:
        print(encode)
        exit(1)

    tables = soup.findAll('table')
    tab = tables[0]

    llast_line = []
    rlast_line = []
    content_temp = []

    for tr in tab.findAll('tr'):
        contents = [] 
        for td in tr.findAll('td'):
            contents.append(td.getText())
        # print(contents)

        left_val = "".join(contents[0]).replace(u'\xa0', u'').replace(' ', '')
        right_val = "".join(contents[2]).replace(u'\xa0', u'').replace(' ', '')

        #same contents
        if(left_val == right_val):
        # if(contents[0] == contents[2]):
            if(lflag != 0 and rflag == 0):
                write_file(file, thead)
                lflag = 0
            if(lflag != 0 and rflag != 0):
                write_file(file, thead)
                lflag = 0
                
            if(rflag != 0):
                if(len(content_temp)):
                    write_file(file, rhead)
                    write_file(file, "\n".join(content_temp))
                    write_file(file, thead)
                rflag = 0
                content_temp.clear()

            if(contents[0] == '\xa0'):
                contents[0] = ''
                contents[2] = ''
            contents[0] = "".join(contents[0]).replace(u'\xa0', u' ')
            contents[2] = "".join(contents[2]).replace(u'\xa0', u' ')
            write_file(file, contents[0])
            lflag = 0
            rflag = 0

        # different contents
        if(left_val != '' and right_val == ''):
        # if(contents[0] != '\xa0' and contents[2] == '\xa0'):
            if(lflag == 0):
                write_file(file, lhead)

            contents[0] = "".join(contents[0]).replace(u'\xa0', u' ')
            write_file(file, contents[0])
            lflag = lflag + 1

        if(left_val == '' and right_val != ''):
        # if(contents[0] == '\xa0' and contents[2] != '\xa0'):
            contents[2] = "".join(contents[2]).replace(u'\xa0', u' ')
            content_temp.append(contents[2])
            rflag = rflag + 1

        if(left_val != right_val and left_val != '' and right_val != ''):
        # if(contents[0] != contents[2] and contents[0] != '\xa0' and contents[2] != '\xa0' ):
            # if( lflag == 0 and rflag != 0):
            #      write_file(file, thead)
                 
            if(lflag == 0):
                write_file(file, lhead)

            contents[0] = "".join(contents[0]).replace(u'\xa0', u' ')
            write_file(file, contents[0])
            lflag = lflag + 1
            contents[2] = "".join(contents[2]).replace(u'\xa0', u' ')
            content_temp.append(contents[2])
            rflag = rflag + 1


if __name__ == "__main__":
    #USAGE:python reduce_repeat_code.py -f1 first_file -f2 second_file -h1 fist_headfile -h2 second_headfile
    my_parser = argparse.ArgumentParser()
    # my_parser.add_argument('-f1', action="store", dest="fname1", required=True)
    # my_parser.add_argument('-f2', action="store", dest="fname2", required=True)
    my_parser.add_argument('-h1', action="store", dest="lhead", required=True)
    my_parser.add_argument('-h2', action="store", dest="rhead", required=True)
    args = my_parser.parse_args()

    thead = "#endif"
    lhead = "#ifdef "+ args.lhead
    rhead = "#ifdef "+ args.rhead
    result_file = "output1.h"

    #if file is existed, clean the file
    if(os.path.exists(result_file) == True):
        with open(result_file, "a+") as f:
            f.seek(0)
            f.truncate()
            f.close()

    #execute the function and calcute the time
    start = time.time()
    try:
        print("==> Writing Into File:" + result_file + "...")
        rewrite_code(result_file, lhead, rhead, thead)
        print("==> OK!!!")
    except Exception as error:
        print("Error:" + str(error))
    end = time.time()
    print("==> Run Time:" + str(end-start) + "s", end='')
