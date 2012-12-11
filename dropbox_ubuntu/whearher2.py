#coding=utf-8
from sys import argv
from urllib import urlopen
from re import S,sub,compile
import re
def getHtml(url):
    page=urlopen(url)
    html=page.read()
    page.close()
    return html
def getWeather(html):
    reg='<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
    weatherList=re.compile(reg,S).findall(html)
    return weatherList
weatherL=getWeather(getHtml('http://gd.weather.com.cn/index.shtml'))
string = ''
for weather in weatherL:
    print weather[1]
