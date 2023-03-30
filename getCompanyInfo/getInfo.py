#!/usr/bin/python3
# coding: utf-8

import requests
import json
from configparser import ConfigParser
import codecs

class Post:
    def sendPost(req_para):
        conf = ConfigParser();
        conf.readfp(codecs.open('config.ini','r','utf-8-sig'));

        #请求参数
        real_data = {}
        real_data["serviceName"] = conf.get('SERVER','serviceName'); #服务名称
        real_data["channelName"] = conf.get('SERVER','channelName'); #渠道名称
        real_data["timeliness"] = conf.get('SERVER','timeliness');
        real_data["autKey"] = conf.get('SERVER','autKey');
        real_data["serviceParam"] = conf.get('SERVER','serviceParam')+json.dumps(req_para);

        #请求头设置    
        head = {"Content-Type":"application/json; charset=UTF-8", 'Connection': 'close'};
        #请求地址
        url = conf['SERVER']['url'];
        jsons = json.dumps(real_data);
        print(jsons);
        #进行请求
        response = requests.post(url=url, data=jsons, headers=head);
        
        #打印返回数据
        print(response.text)
        response_dict = json.loads(response.text);
        if len(json.loads(response_dict['data'])['data']) != 0:
            return json.loads(response_dict['data'])['data'][0]['TDATA'];
        else:
            return [];
