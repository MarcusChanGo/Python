#!/usr/bin/python3
# coding: utf-8

import requests
import json
from configparser import ConfigParser

class Post:
    def sendPost(req_para):
        conf = ConfigParser();
        conf.read('config.ini');

        #请求参数
        real_data = {}
        real_data["serviceName"] = conf['SERVER']['serviceName']; #服务名称
        real_data["channelName"] = conf['SERVER']['channelName']; #渠道名称
        real_data["timeliness"] = conf['SERVER']['timeliness'];
        real_data["autKey"] = conf['SERVER']['autKey'];
        real_data["serviceParam"] = conf['SERVER']['serviceParam']+json.dumps(req_para);

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
