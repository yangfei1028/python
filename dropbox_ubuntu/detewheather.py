#coding:utf-8
#coder:shiweifu@gmail.com
import string
import urllib
import sys

def getWeather(to):
    dic = {"from": "0", 
       "uid": "frontui_1266379660_6450", 
       "pu": "pd%401%2Csz%40176_208%2Cuc%400", 
       "word": "0312", 
       "ct_6": "%E5%A4%A9%E6%B0%94%E6%9F%A5%E8%AF%A2", 
       "bd_page_type": "1", 
       "tn_1": "webmain", 
       "tn_6": "weather", 
       "st_6": "106001", 
       "st_1": "111041", 
       "ssid": "0"}
    
    dic["word"] = str(to)
    
    url = "http://m.baidu.com/s?"
    url = url + urllib.urlencode(dic)
    print url
    s = urllib.urlopen(url).readlines()[17]
    #去除两边空格
    s = s.strip()
    #查找所在地区
    s = s[s.find(">")+1:]
    tmp = s.find("<br/>")
    address = s[:tmp]
    s = s[tmp+len("<br/>"):]
    #今天天气
    tmp = s.find("<br/>")
    today = s[:tmp]
    s = s[tmp+len("<br/>"):]
    #明天天气
    tmp = s.find("<br/>")
    tomorrow = s[:tmp]
    s = s[tmp+len("<br/>"):]
    #获取提供
    tmp = s.find("[")+1
    fro = s[tmp:s.find("]")]
    
    return {"from":fro,"tomorrow":tomorrow,"today":today,"city":address}
    

def main():
    weather = getWeather("0371")
    print weather["tomorrow"]
    print weather

if __name__ == "__main__":
    main()
