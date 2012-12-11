import MySQLdb as mdb

con = None

try:
    #连接mysql的方法：connect('ip','user','password','dbname')
    con = mdb.connect('localhost', 'root','2007113', 'test');

    #所有的查询，都在连接con的一个模块cursor上面运行的
    cur = con.cursor()

    #执行一个查询
    cur.execute("SELECT VERSION()")

    #取得上个查询的结果，是单个结果
    data = cur.fetchone()
    print "Database version : %s " % data
finally:
    if con:
        #无论如何，连接记得关闭
        con.close()
