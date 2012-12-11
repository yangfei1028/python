#获取贴吧列表或某列表
import urllib
import re
import sys
type = sys.getfilesystemencoding()
#print myname.decode('UTF-8').encode(type)
pager=urllib.urlopen('http://tieba.baidu.com/f?kw=%B7%B2%C8%CB%D0%DE%CF%C9%B4%AB&fr=ala0')
data=pager.read()
m=re.findall(r'<[^>]* class="j_th_tit">(第十一卷 真仙降世[\s\S]+?)</a>',data)
#m=re.findall(r'<[^>]* class="j_th_tit">([\s\S]+?)</a>',data)
s = ''
for i in m:
     print i
     s+=i+'\r\n'

#f=open(r"i:\2.txt",'w')
#f.write(s)
#f.close()
