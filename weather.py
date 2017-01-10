#! /usr/bin/env python3
# encoding:utf-8

import requests,json,re
from pprint import pprint

with open('/etc/conky/config.json') as f:
    config=f.read()
    c_json=json.loads(config)
    city=c_json["city"]
    ak=c_json["ak"]

baidu_url='http://api.map.baidu.com/telematics/v3/weather?location='+city+'&output=json&ak='+ak

r=requests.get(baidu_url)

t=json.loads(r.text)

weather_data=t['results'][0]['weather_data']

tody=weather_data[0]
pattern = re.compile(r'\(.*\)')
rt=pattern.search(tody['date'])

tomm=weather_data[1]
tdat=weather_data[2]
tdft=weather_data[3]


print ('今天',tody['temperature'],tody['weather'],rt.group(0))
print (tomm['date'],tomm['temperature'],tomm['weather'])
print (tdat['date'],tdat['temperature'],tdat['weather'])
print (tdft['date'],tdft['temperature'],tdft['weather'])
