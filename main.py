# -*- coding: UTF-8 -*-
from urllib import urlopen
import re



def getfilecontent(begin,data,num): 
    filterstr = "\[点击右键另存为\](.*)本栏目更多同类内容"
    p = re.compile(filterstr,re.DOTALL)
    url = "http://www.hxen.com/englishlistening/xingainian/4/" + data + "/" + str(num) + ".html"
    text = urlopen(url).read()
    a = text.decode("gb2312").encode('utf8')
    result = "".join(p.findall(a))#将信息提取到模式1和模式2（即两个括号里的内容）
    filenum = num - begin + 1
    with open(str(filenum) + '.txt','a') as f:
        for cell in result.split("</p>"):
            if not (cell.find("<p>") != -1 or cell.find("<br />") != -1):
                pass
            else:  
                string = cell.replace("&nbsp;","").replace("<p>","").replace("<br />","\n")
                f.write(string)
                #print string

#getfilecontent(88)

def getallfile():
    for i in range(1318,1366,1):
        print i
        try:
            getfilecontent(1318,'2007-03-21',i)
        except:
            print i

getallfile()
#getfilecontent(1258,'2007-03-21',1317)
        