# -*- coding: cp936 -*-

import sys,urllib2,re
def GetWeather(city):
   url = 'http://php.weather.sina.com.cn/search.php?city='+city+'&dpc=1'
   response = urllib2.urlopen(url)
   result=response.read() 
 
   data = []
   #�ҳ�����
   cityname = re.findall(r'<div class="nav21">([\s\S]+?)<\/div>',result)
   print cityname
   if len(cityname) > 0:
        city = filterHtmlTags(cityname[0])
   #����
   try:
        data.append(re.findall(r'<h2>([\s\S]+?)<\/h2>'),result)
   except IndexError:
        data.append('��������')
   #�¶�
   try:
        data.append(re.findall(r'<div class="w-number">([\s\S]+?)<\/div>'),result)
   except IndexError:
        data.append('��������')
   #����
   try:
        data.append(re.findall(r'<li>����([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('��������')
   #����
   try:
        data.append(re.findall(r'<li>������([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('��������')
   #������
   try:
        data.append(re.findall(r'<li>�����ߣ�([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('��������')
   #���ʶ�
   try:
        data.append(re.findall(r'<li>���ʶȣ�([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('��������')
   #��ɹָ��
   try:
        data.append(re.findall(r'<li>��ɹָ����([\s\S]+?)<\/li>'),result)
   except IndexError:
        data.append('��������')
   #����
   t = []
   t.append(re.findall(r'<p>������([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>�¶ȣ�([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>������([\s\S]+?)<\/p>'),result)
   data.append(t)
   #����
   t = []
   t.append(re.findall(r'<p>������([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>�¶ȣ�([\s\S]+?)<\/p>'),result)
   t.append(re.findall(r'<p>������([\s\S]+?)<\/p>'),result)
   data.append(t)
   for a in range(len(data)):
        data[a] = filterHtmlTags(data[a])
   result = "����:\t%s\n----��������----\n����:\t%s\n�¶�:\t%s\n����:\t%s\n����:\t%s\n������:\t%s\n���ʶ�:\t%s\n��ɹָ��:\t%s\n----��������----\n����:\t%s\n�¶�:%s\n����:%s\n----��������----\n����:%s\n�¶�:%s\n����:%s\n" % (city,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7][0],data[7][1],data[7][2],data[8][0],data[8][1],data[8][2])
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
#     city = raw_input('����������� >>> ')
#     if len(city) == 0 :
#         print '�˳�'
#         sys.exit(0)
      GetWeather('shanghai')
