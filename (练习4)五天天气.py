# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:52:20 2018

@author: 果芽芽
"""
url=('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric')
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#五天的天气
print('第一天')
print(data['list'][2]['weather'][0]['main'])
print(data['list'][2]['main']['temp'])
print(data['list'][2]['main']['pressure'])
print(data['list'][2]['main']['temp_min'])
print(data['list'][2]['main']['temp_max'])
print('第二天')
print(data['list'][10]['weather'][0]['main'])
print(data['list'][10]['main']['temp'])
print(data['list'][10]['main']['pressure'])
print(data['list'][10]['main']['temp_min'])
print(data['list'][10]['main']['temp_max'])
print('第三天')
print(data['list'][18]['weather'][0]['main'])
print(data['list'][18]['main']['temp'])
print(data['list'][18]['main']['pressure'])
print(data['list'][18]['main']['temp_min'])
print(data['list'][18]['main']['temp_max'])
print('第四天')
print(data['list'][26]['weather'][0]['main'])
print(data['list'][26]['main']['temp'])
print(data['list'][26]['main']['pressure'])
print(data['list'][26]['main']['temp_min'])
print(data['list'][26]['main']['temp_max'])
print('第五天')
print(data['list'][34]['weather'][0]['main'])
print(data['list'][34]['main']['temp'])
print(data['list'][34]['main']['pressure'])
print(data['list'][34]['main']['temp_min'])
print(data['list'][34]['main']['temp_max'])

#
print('温度折线图如下：')
print('第一天'+'-'*int(data['list'][2]['main']['temp']))
print('第二天'+'-'*int(data['list'][2]['main']['temp']))
print('第三天'+'-'*int(data['list'][2]['main']['temp']))
print('第四天'+'-'*int(data['list'][2]['main']['temp']))
print('第五天'+'-'*int(data['list'][2]['main']['temp']))
#
print('排序如下：')
temper=[data['list'][2]['main']['temp'],
       data['list'][10]['main']['temp'],
       data['list'][18]['main']['temp'],
       data['list'][26]['main']['temp'],
       data['list'][34]['main']['temp']]
print(sorted(temper))
















