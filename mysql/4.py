# -*- coding: UTF-8 -*-
# 来源：疯狂的蚂蚁的博客www.crazyant.net总结整理

import MySQLdb as mdb
import sys

#获得mysql查询的链接对象
con = mdb.connect('localhost', 'root', '2007113', 'test')

with con:
    #获取连接上的字典cursor，注意获取的方法，
    #每一个cursor其实都是cursor的子类
    cur = con.cursor(mdb.cursors.DictCursor)

    #执行语句不变
    cur.execute("SELECT * FROM Writers")

    #获取数据方法不变
    rows = cur.fetchall()

    #遍历数据也不变（比上一个更直接一点）
    for row in rows:
        #这里，可以使用键值对的方法，由键名字来获取数据
        print "%s %s" % (row["Id"], row["Name"])
