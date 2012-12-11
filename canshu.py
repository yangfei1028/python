#函数中列表默认参数中为列表类型，调用后值有保留
def info(a,b):
     c=[]
     print a,b
     print c
     c.insert(11,'a')
def info2(a,b,c=[]):     
     print a,b
     print c
     c.insert(11,'a')

info(1,2)
info(1,2)
info2(1,2)
info2(1,2)
