#!/usr/bin/python3
# coding: utf-8

from read_file import readWriteFile;
from getInfo import Post;
from configparser import ConfigParser
import codecs


if __name__=="__main__":
    conf = ConfigParser();
    conf.readfp(codecs.open('config.ini','r','utf-8'));

    # 获取公司名称和统一社会信用代码
    companyName = readWriteFile.readFile(conf.get('FILE','inputfile'));
    companyNameList = companyName['客户名称'].tolist();
    socialCodeList = companyName['统一社会信用代码'].tolist();

    resultData = [];
    # 通过公司名称和统一社会信用代码获取其他信息
    for name, code in zip(companyNameList,socialCodeList):
        reqData = {
            "keyType":"32",
        };
        reqData["key"] = name;
        reqData["model"] = "ENTINFO";
        respData = {};
        # 调用外部数据平台服务接口（企业基本信息ENTINFO）
        TDATA = Post.sendPost(reqData);
        print("调用企业基本信息服务");
        respData['companyname'] = name;
        respData['creditcode'] = code;
        respData['creditcode_a'] = TDATA[0]['CREDITCODE'];
        respData['dom'] = TDATA[0]['DOM'];
        respData['empnum'] = TDATA[0]['EMPNUM'];
        respData['entstatus'] = TDATA[0]['ENTSTATUS'];
        respData['esdate'] = TDATA[0]['ESDATE'];
        respData['frname'] = TDATA[0]['FRNAME'];
        respData['industrycocode'] = TDATA[0]['INDUSTRYCOCODE'];
        respData['industryconame'] = TDATA[0]['INDUSTRYCONAME'];
        respData['orgcodes'] = TDATA[0]['ORGCODES'];
        respData['tel'] = TDATA[0]['TEL'];
        respData['zsopscope'] = TDATA[0]['ZSOPSCOPE'];
        
        # 调用外部数据平台服务接口（股东信息SHAREHOLDER）
        reqData['model'] = 'SHAREHOLDER';
        print("调用股东信息服务");
        TDATA_1 = Post.sendPost(reqData);
        if len(TDATA_1) != 0:
            respData['shaname'] = TDATA_1[0]['SHANAME'];

        # 调用外部数据平台服务接口（税务开票信息INVOICEINFO）
        reqData['model'] = 'INVOICEINFO';
        print("调用税务开票信息服务");
        TDATA_2 = Post.sendPost(reqData);
        if len(TDATA_2) != 0:
            respData['bankaccount'] = TDATA_2[0]['BANKACCOUNT'];
            respData['bankaccountname'] = TDATA_2[0]['BANKACCOUNTNAME'];
            respData['bankname'] = TDATA_2[0]['BANKNAME'];

        # 调用外部数据平台服务接口（公示许可PUBLICENSE）
        reqData['model'] = 'PUBLICENSE';
        print("调用公示许可服务");
        TDATA_3 = Post.sendPost(reqData);
        if len(TDATA_3) != 0:
            respData['swdj'] = TDATA_3[0]['C_SWDJ'];
    
        resultData.append(respData);

    fileName = conf.get('FILE','outputfile');
    readWriteFile.pd_toExcel(resultData, fileName);
    print("获取数据完成！！！");
    