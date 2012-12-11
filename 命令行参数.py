import sys
if __name__ == '__main__':
     start = int(sys.argv[1])
     end = int(sys.argv[2])
     data = open('picmedia.py','r')
     data_list=data.readlines()
     data.close()

     for line in data_list[start:end]:
          print line.strip()
