#coding=utf-8
from sys import argv
from urllib import urlopen
from re import S,sub,compile
def format_reports(s):
    s = sub("/s+",' ',s)
    s = sub(" ",' ',s)
    s = sub("<[^>]*>",' ',s)
    return s
def weather_report(searchurl):
    string = ''
    searchurl = 'http://www.weather.com.cn/html/weather/101110101.shtml'
    html = urlopen(searchurl).read()
    day1weather = compile('<!--day 1-->(.*?)<!--day 2-->',S).findall(html)
    day2weather = compile('<!--day 2-->(.*?)<!--day 3-->',S).findall(html)
    day3weather = compile('<!--day 3-->(.*?)<!--day 4-->',S).findall(html)
    day4weather = compile('<!--day 4-->(.*?)<!--day 5-->',S).findall(html)
    for result in day1weather:
        string += ' '.join(format_reports(result).split())
    string += '。'
    for result in day2weather:
        string += ' '.join(format_reports(result).split())
    string += '。'
    for result in day3weather:
        string += ' '.join(format_reports(result).split())
    string += '。'
    for result in day4weather:
        string += ' '.join(format_reports(result).split())
    string += '。'
    return string
if __name__ == '__main__':
    xianmessage = weather_report('http://www.weather.com.cn/html/weather/101110101.shtml')
    print xianmessage+ '/n'
    xianyangmessage = weather_report('http://www.weather.com.cn/html/weather/101110200.shtml')
    print xianyangmessage + '/n'
    hangzhoumessage = weather_report('http://www.weather.com.cn/html/weather/101210101.shtml')
    print hangzhoumessage + '/n'
    weihaimessage = weather_report('http://www.weather.com.cn/html/weather/101121301.shtml')
    print weihaimessage + '/n'
    URL = 'http://quanapi.sinaapp.com/fetion.php?u=18858298271&p=wang113.&to=%s&m=%s'
    urlopen(URL%('18858298271','杭州:' + hangzhoumessage))
#   urlopen(URL%('15868470646','杭州:' + hangzhoumessage))
#   urlopen(URL%('18858298271','西安:' + xianmessage))
#   urlopen(URL%('18858298271','咸阳:' + xianyangmessage))
#   urlopen(URL%('18858298271','威海:'+ weihaimessage))
    print 'Sucessce!'
#   raw_input()
