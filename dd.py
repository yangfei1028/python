# -*- coding: cp936 -*-
import sys,urllib2,re
city = 'shanghai'
url = 'http://php.weather.sina.com.cn/search.php?city='+city+'&dpc=1'
response = urllib2.urlopen(url)
result=response.read() 
 
data = []


data.append(re.findall(r'<h2>([\s\S]+?)<\/h2>'),result)
print data
