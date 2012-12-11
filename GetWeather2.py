# -*- coding: cp936 -*-

import sys,urllib2,re
def GetWeather(city):
   url = 'http://php.weather.sina.com.cn/search.php?city='+city+'&dpc=1'
   response = urllib2.urlopen(url)
   result=response.read() 
 
   data = []
   #找城市名
   cityname = re.findall(r'<div class="nav21">([\s\S]+?)<\/div>',result)
   print cityname
   if len(cityname) > 0:
        city = filterHtmlTags(cityname[0])
   #天气
   try:
        data.append(re.findall(r'<h2>([\s\S]+?)<\/h2>'),result)
   except IndexError:
        data.append('暂无数据')
   #温度
   try:
        data.append(re.findall(r'<div class="w-number">([\s\S]+?)<\/div>'),result)
   except IndexError:
        data.append('暂无数据')
   #风向
   try:
        data.append(re.findall(r'<li>风向：([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('暂无数据')
   #风力
   try:
        data.append(re.findall(r'<li>风力：([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('暂无数据')
   #紫外线
   try:
        data.append(re.findall(r'<li>紫外线：([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('暂无数据')
   #舒适度
   try:
        data.append(re.findall(r'<li>舒适度：([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('暂无数据')
   #防晒指数
   try:
        data.append(re.findall(r'<li>防晒指数：([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('暂无数据')
   #明天
   t = []
   t.append(re.findall(r'<p>天气：([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>温度：([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>风力：([\s\S]+?)<\/p>'),result)
   data.append(t)
   #后天
   t = []
   t.append(re.findall(r'<p>天气：([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>温度：([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>风力：([\s\S]+?)<\/p>'),result)
   data.append(t)
   for a in range(len(data)):
        data[a] = filterHtmlTags(data[a])
   result = "城市:\t%s\n----今日天气----\n天气:\t%s\n温度:\t%s\n风向:\t%s\n风力:\t%s\n紫外线:\t%s\n舒适度:\t%s\n防晒指数:\t%s\n----明日天气----\n天气:\t%s\n温度:%s\n风力:%s\n----后天天气----\n天气:%s\n温度:%s\n风力:%s\n" % (city,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7][0],data[7][1],data[7][2],data[8][0],data[8][1],data[8][2])
   print result
def filterHtmlTags(a):
     if isinstance(a,basestring):
          a = re.sub(r'<[^>]+>','',a)
          a = re.sub(r'\s+','',a)
     if isinstance(a,list):
          for i in range(len(a)):
               a[i] = filterHtmlTags(a[i])
     return a
if __name__=="__main__":
#   while True:
#     city = raw_input('请输入城市名 >>> ')
#     if len(city) == 0 :
#         print '退出'
#         sys.exit(0)
      GetWeather('shanghai')
