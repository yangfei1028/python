#coding=utf-8
from sys import argv
from urllib import urlopen
from re import S,sub,compile
def format_reports(s):
#    s = sub("/s+",' ',s)
    s = sub(" ",' ',s)
#   s = sub("<[^>]*>",' ',s)
    s = sub('<*>',' ',s)     
    return s
string = ''
searchurl = 'http://www.weather.com.cn/html/weather/101110101.shtml'
html = urlopen(searchurl).read()
day1weather = compile('<!--day 1-->(.*?)<!--day 2-->',S).findall(html)
for result in day1weather:
     string += ' '.join(format_reports(result).split())
print string
