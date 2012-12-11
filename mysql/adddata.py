# -*- coding: UTF-8 -*-
# 来源于www.crazyant.net总结整理
import MySQLdb as mdb
import sys

#将con设定为全局连接
con = mdb.connect('localhost', 'root', '2007113', 'test');

with con:

    #获取连接的cursor，只有获取了cursor，我们才能进行各种操作
    cur = con.cursor()
    #创建一个数据表 writers(id,name)
    cur.execute("CREATE TABLE IF NOT EXISTS \
        Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
    #以下插入了5条数据
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
