#!/usr/bin/python3
# coding: utf-8

from sqlite3_pro import sqlite_db
from read_file import readWriteFile

class analyse:
    def test_function():
        print("Connect the database data.db");

        str_sql = '''CREATE TABLE index_data (
                    id integer primary key,
                    index_code varchar(30) not null,
                    index_name varchar(100) not null,
                    company_code varchar(50) not null,
                    company_name varchar(100) not null,
                    var  varchar(200)
                );'''
        sqlite_db.create_table(str_sql);

        print("read excel data to sqlite3.");
        result = readWriteFile.readFile();

        str_tab = '''
            INSERT INTO index_data (id,index_code,index_name,company_code,company_name,var)
            VALUES(NULL,?,?,?,?,?);
            ''';
        

        # print(result._stat_axis.values.tolist());
        # print(result.columns.values.tolist());
        # print(result.values);
        # print(len(result.values));
        colValues = [];
        for ind, val in enumerate(result.values):
            # print(type(val));
            if ind == 0:
                company_name = val.tolist();
                all_name = val.tolist();
                del company_name[0:2];
                # print(company_name);
            elif ind == 1:
                company_code = val.tolist();
                del company_code[0:2];

                all_code = val.tolist();
                i = 0;
                row1Values = [];
                row2Values = [];
                for name,code in zip(company_name,company_code):
                    row1 = [];
                    row2 = []
                    row1.append(all_name[0]);
                    row1.append(all_name[1]);
                    row1.append(code);
                    row1.append(name);
                    row1.append(all_name[i+2]);
                    row1Values.append(tuple(row1));
                    
                    row2.append(all_code[0]);
                    row2.append(all_code[1]);
                    row2.append(code);
                    row2.append(name);
                    row2.append(all_code[i+2]);
                    row2Values.append(tuple(row2));
                    
                    i = i+1;
                # 新增公司名称
                sqlite_db.insertMultValue(str_tab, row1Values);
                # 新增公司社保号
                sqlite_db.insertMultValue(str_tab, row2Values);
                # print(company_code);
            else:
                # temp = val.tolist();
                i = 0;
                for name,code in zip(company_name,company_code):
                    col = [];
                    col.append(val[0]);
                    col.append(val[1]);
                    col.append(code);
                    col.append(name);
                    col.append(val[i+2]);
                    i = i+1;
                    # print(col);
                    colValues.append(tuple(col));

                # print(colValues);

        # 新增到数据库
        sqlite_db.insertMultValue(str_tab, colValues);
        print("Done!!!");
