#!/usr/bin/python3
# coding: utf-8

import sqlite3
from sqlite3 import OperationalError


class sqlite_db:
    # 连接数据库
    def conn_db():
        conn = sqlite3.connect('./data/data.db');
        return conn;

    # 创建数据库
    def create_db():
        pass; 
    
    # 创建表
    def create_table(sql):
        conn = sqlite_db.conn_db();
        cur = conn.cursor();
        try:
            cur.execute(sql);
            print("create table success");
        except OperationalError as o:
            print(str(o));
            pass
            if str(o) == "table gas_price already exists":
                print("table gas_price already exists");
        except Exception as e:
            print(e);
        finally:
            cur.close();
            conn.close();


    # 新增单条记录
    def insertSingleValue(str_tab, str_sql):
        conn = sqlite_db.conn_db();
        cur = conn.cursor();    
        cur.execut(str_tab,str_sql);
        print("Command executed successfully!");
        conn.commit();
        cur.close();
        conn.close();

    # 新增多条记录
    def insertMultValue(str_sql, values):
        conn = sqlite_db.conn_db();
        cur = conn.cursor();    
        cur.executemany(str_sql, values);
        print("Command executed successfully!");
        conn.commit();
        cur.close();
        conn.close();

    # 删除所有记录
    def deleteAll():
        conn = sqlite_db.conn_db();
        cur = conn.cursor();    
        cur.execut("ddelete from index_data;");
        print("Command executed successfully!");
        conn.commit();
        conn.close();