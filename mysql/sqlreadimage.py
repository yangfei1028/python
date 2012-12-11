#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb 
import sys
try:
    conn = mdb.connect(host='localhost',user='root', 
        passwd='2007113', db='test')
    cursor = conn.cursor()
    cursor.execute("SELECT Data FROM images LIMIT 1")
    fout = open('22.txt','wb')
    fout.write(cursor.fetchone()[0])
    fout.close()
    cursor.close()
    conn.close()

except IOError, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
