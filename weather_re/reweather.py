#coding=utf-8
from sys import argv
from urllib import urlopen
from re import S,sub,compile
import re
def getWeather2(): 
    '''
        从qq.ip138.com 取得天气数据(html格式), 输出为xml格式
    '''
    #相应参数:如果网址参数发生变化, 修改以下部分
    ############################################

    URL = "http://qq.ip138.com/weather/zhejiang/HangZhou.htm"

    ############################################

    reDay = re.compile(r'(?<=日期).*星期.+?(?=</tr>)', 
            re.I|re.S|re.U)
    reWeather = re.compile(r'(?<=align\="center">天气</td>).+?(?=</tr)',
            re.I|re.S|re.U)
    reTemperature = re.compile(r'(?<=align\="center">气温</td>).+?(?=</tr)',
            re.I|re.S|re.U)
    reWind = re.compile(r'(?<=align\="center">风向</td>).+?(?=</tr)',
            re.I|re.S|re.U)
    rePic = reWeather
    reEachDay = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})',re.I|re.S|re.U)
    print reEachDay
    weadata = []
    for i in range(12):
        weadata.append(u'')
    try: 
        #获取网页源文件 
        sock = urllib.urlopen(URL)
        print sock
        strhtml = sock.read()
        print strhtml
        strhtml = unicode(strhtml, 'gb2312','ignore').encode('utf-8','ignore') 
        print strhtml
        # 正则表达式取得各段
        dayPara = re.findall(reDay, strhtml)
        weatherPara = re.findall(reWeather, strhtml)
        temperaturePara = re.findall(reTemperature, strhtml)
        windPara = re.findall(reWind, strhtml)
        picPara = re.findall(rePic, strhtml)
        #获取日期
        theDays= re.findall(reEachDay, dayPara[0]) 
        firstDay = datetime.datetime.strptime(theDays[1],'%Y-%m-%d')
        nextDay = firstDay + datetime.timedelta(1)
        lastDay = firstDay + datetime.timedelta(2)
        
        weadata[0] = u'2'
        weadata[1] = unicode(theDays[0].replace('-', '/'))
        weadata[2] = unicode(firstDay.month)+u'月'+unicode(firstDay.day)+u'日 '
        weadata[6] = unicode(nextDay.month)+u'月'+unicode(nextDay.day)+u'日 '
        weadata[9] = unicode(lastDay.month)+u'月'+unicode(lastDay.day)+u'日 '

        #获取天气概况
        theWeathers= re.findall(r'(?<=br/>).+?(?=</td)',weatherPara[0])
        print theWeathers
        weadata[2] += unicode(theWeathers[1].decode('utf-8')) 
        weadata[6] += unicode(theWeathers[2] .decode('utf-8'))
        weadata[9] += unicode(theWeathers[3] .decode('utf-8'))
        # 获取温度信息
        # [0] 当前温度 [1]明日最高 [2]明日最低[3]后日最高[4]后日最低
        theGrades = re.findall('(-?\d+℃)', temperaturePara[0]) 
        weadata[3] = unicode(theGrades[2].decode('utf-8')
                ) + u'/' +unicode(theGrades[3].decode('utf-8')) 
        weadata[7] = unicode(theGrades[4].decode('utf-8')
                ) + u'/' +unicode(theGrades[5].decode('utf-8')) 
        weadata[10] = unicode(theGrades[6].decode('utf-8')
                ) + u'/' +unicode(theGrades[7].decode('utf-8')) 
        #获取风向
        # [0] 当前风向 [1]明日 [2]后日
        theWinds = re.findall(r'(?<=td>).+?(?=</td>)', windPara[0])
        weadata[4] = unicode(theWinds[1].decode('utf-8'))
        #获取天气图标
        thePics = re.findall(r'/image/(..\.gif)"', picPara[0])
        weadata[5] = unicode(thePics[1].decode('utf-8'))
        weadata[8] = unicode(thePics[2].decode('utf-8'))
        weadata[11] = unicode(thePics[3].decode('utf-8'))
        print weadata
        
        listToxml(weadata, "template/wea2.xml")
        log('weather2获取天气信息成功', 'logs/running.log')
    except Exception, ex: 
        #如果错误, 记入日志
        log('严重错误:weather2获取xml文件失败')
        errlog('getWeather2', ex, sys.exc_info())
        log('weather2获取xml文件失败', 'logs/running.log')
        return False
    return True
if __name__ == '__main__':
    getWeather2()
