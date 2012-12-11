#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb 
import sys
try:
    conn = mdb.connect(host='localhost',user='testuser', 
        passwd='test623', db='testdb')
    cursor = conn.cursor()
    #cursor.execute( "SELECT PicData FROM Dem_Picture ORDER BY ID DESC limit 1")
    cursor.execute( "SELECT Data FROM  images limit 1")
    d = cursor.fetchone()[0]
    fout = open('2hhfgh3.png','wb')
    fout.write(d)
    fout.close()
    cursor.close()
    conn.close()

except IOError, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
