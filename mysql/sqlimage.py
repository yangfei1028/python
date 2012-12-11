# -*- coding: UTF-8 -*-
# 来源：疯狂的蚂蚁的博客www.crazyant.net总结整理
import MySQLdb as mdb
import MySQLdb
import sys

try:
    #用读文件模式打开图片
    fin = open("1.png")
    #将文本读入img对象中
    img = fin.read()
    #关闭文件
    fin.close()

except IOError, e:
    #如果出错，打印错误信息
    print "Error0 %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

try:
    #链接mysql，获取对象
    conn = mdb.connect(host='localhost',user='root',passwd='2007113', db='test')
    #获取执行cursor
    cursor = conn.cursor()
    #直接将数据作为字符串，插入数据库
    cursor.execute("INSERT INTO images SET Data='%s'" %\
                   MySQLdb.escape_string(img))

    #提交数据
    conn.commit()

    #提交之后，再关闭cursor和链接
    cursor.close()
    conn.close()

except mdb.Error, e:
    #若出现异常，打印信息
    print "Error1 %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
