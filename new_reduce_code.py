#!/bin/env python
#--*--coding:utf-8 --*--

import os
import re
import sys
import difflib
import argparse
from bs4 import BeautifulSoup


# write file 
def write_file(file, content):
    result_file = open(file, 'a')
    result_file.write(content + "\n")
    result_file.close()

#analyze file and output result
def rewrite_code(file, lhead, rhead, thead):
    flag = 0
    lflag = 0
    rflag = 0
    url = "Report.html"
    soup = BeautifulSoup(open(url, 'r', encoding='utf-8'), "html.parser")
    tables = soup.findAll('table')
    tab = tables[0]

    llast_line = []
    rlast_line = []
    content_temp = []
    for tr in tab.findAll('tr'):
        contents = [] 
        for td in tr.findAll('td'):
            contents.append(td.getText())
        print("---->")
        print(contents)

        #same contents
        if(contents[0] == contents[2]):
            if(flag != 0):
                write_file(file, thead)
                flag = 0

            if(rflag != 0):
                write_file(file, rhead)
                write_file(file, "\n".join(content_temp))
                write_file(file, thead)
                rflag = 0
                content_temp.clear()

            write_file(file, contents[0]) 

        #different contents
        if(contents[0] != '\xa0' and contents[2] == '\xa0'):
            if(rflag != 0):
                write_file(file, thead)
                flag = 0
            if(rflag != 0):
                write_file(file, rhead)
                write_file(file, "\n".join(content_temp))
                write_file(file, thead)
                rflag = 0
                content_temp.clear()

            if (flag == 0 and contents[0] != '\xa0'):
                write_file(file, lhead)
                
            if(contents[0] == '\xa0'):
                continue

            write_file(file, contents[0])
            flag = flag + 1

        if(contents[0] == '\xa0' and contents[2] != '\xa0'):
            # if(flag != 0):
            #     write_file(file, thead)
            #     flag = 0
            if(rflag != 0):
                write_file(file, rhead)
                write_file(file, "\n".join(content_temp))
                write_file(file, thead)
                rflag = 0
                content_temp.clear()

            if (flag == 0 and contents[2] != '\xa0'):
                write_file(file, rhead)
                
            if(contents[2] == '\xa0'):
                continue

            write_file(file, contents[2])
            flag = flag + 1

        if(contents[0] != contents[2] and contents[0] != '\xa0' and contents[2] != '\xa0' ):
            # if(flag != 0):
            #     write_file(file, thead)
            if(flag == 0):
                write_file(file, lhead)

            if(contents[2] == '\xa0' or contents[2] == '\xa0'):
                continue

            write_file(file, contents[0])
            flag = flag + 1

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

    out_file = "compare_file.html"

    # file1 = args.fname1
    # file2 = args.fname2
    # compare_file(file1, file2, out_file)

    thead = "#endif"
    lhead = "#ifndef "+ args.lhead +"\n" + "#define " + args.lhead
    rhead = "#ifndef "+ args.rhead +"\n" + "#define " + args.rhead

    result_file = "output.h"
    #if file existed, clean the file
    if(os.path.exists(result_file) == True):
        with open(result_file, "a+") as f:
            f.seek(0)
            f.truncate()
            f.close()

    print("WRITING INTO '" + result_file + "'...")
    rewrite_code(result_file, lhead, rhead, thead)
    print("========> SUCCESS!")
