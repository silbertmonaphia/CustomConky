#! /usr/bin/env python3
# encoding:utf-8

import requests,json
from pprint import pprint

city='广州'
ak='Om8o9AoznNvN6H7ofLcMB12Q2td5h0G4'
baidu_url='http://api.map.baidu.com/telematics/v3/weather?location='+city+'&output=json&ak='+ak

r=requests.get(baidu_url)

t=json.loads(r.text)

weather_data=t['results'][0]['weather_data']

tody=weather_data[0]
tomm=weather_data[1]
tdat=weather_data[2]
tdft=weather_data[3]

print ('今天',tody['temperature'],'  明天',tomm['temperature'])
print ('后天',tdat['temperature'],'  大后天',tdft['temperature'])
