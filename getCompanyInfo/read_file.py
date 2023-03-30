#!/usr/bin/python3
# coding: utf-8

import pandas as pd


class readWriteFile:  
    def readFile(file_name):
        print("begin read!!");
        result = pd.read_excel(file_name, sheet_name='Sheet1');
        return result;
    

    def writeFile(schemal_name, info_list, file_name):
        df = pd.DataFrame(info_list);
        df.index.name = '序号';
        df.rename(columns=schemal_name, inplace=True);
        df.to_excel(file_name);
        return
    

    def pd_toExcel(data, fileName):  # pandas库储存数据到excel
        companyname = [];
        creditcode = [];
        dom = [];
        empnum = [];
        entstatus = [];
        esdate = [];
        frname = [];
        industrycocode = [];
        industryconame = [];
        orgcodes = [];
        tel = [];
        zsopscope = [];
        shaname = [];
        bankaccount = [];
        bankaccountname = [];
        bankname = [];
        swdj = [];
        creditcode_a = [];
        for i in range(len(data)):
            companyname.append(data[i]["companyname"]);
            creditcode.append(data[i]["creditcode"]);
            dom.append(data[i]["dom"]);
            empnum.append(data[i]["empnum"]);
            entstatus.append(data[i]["entstatus"]);
            esdate.append(data[i]["esdate"]);
            frname.append(data[i]["frname"]);
            industrycocode.append(data[i]["industrycocode"]);
            industryconame.append(data[i]["industryconame"]);
            orgcodes.append(data[i]["orgcodes"]);
            tel.append(data[i]["tel"]);
            zsopscope.append(data[i]["zsopscope"]);
            shaname.append(data[i]["shaname"]);
            bankaccount.append(data[i]["bankaccount"]);
            bankaccountname.append(data[i]["bankaccountname"]);
            bankname.append(data[i]["bankname"]);
            swdj.append(data[i]["swdj"]);
            creditcode_a.append(data[i]["creditcode_a"]);
        dfData = {  # 用字典设置DataFrame所需数据
            '客户名称': companyname,
            '统一社会信用代码': creditcode,
            '住址': dom,
            '员工人数': empnum,
            '经营状态': entstatus,
            '成立日期': esdate,
            '法定代表人/负责人/执行事务合伙人': frname,
            '国民经济行业代码': industrycocode,
            '国民经济行业名称': industryconame,
            '组织机构代码': orgcodes,
            '联系人电话': tel,
            '经营业务范围': zsopscope,
            '股东名称': shaname,
            '银行账户': bankaccount,
            '银行账户名称': bankaccountname,
            '银行名称': bankname,
            '税务登记号码': swdj,
            '统一社会信用代码': creditcode_a
        }
        df = pd.DataFrame(dfData)  # 创建DataFrame
        df.to_excel(fileName, index=False)
