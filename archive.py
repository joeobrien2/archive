## Joe O'Brien
## 2/22/13
## Script to help updating the province news archive pages on the intranet. It will rename Province_News_Archives_2.html to 3, 1 to 2, and the current news page to 1

import os, shutil,re

webdir='c:\web sites\intranet'
files=os.listdir(os.curdir)

shutil.copy2(webdir+'\Province_News_Archives_2.html', webdir+'\Province_News_Archives_3.html')
shutil.copy2(webdir+'\Province_News_Archives_1.html', webdir+'\Province_News_Archives_2.html')
shutil.copy2(webdir+'\Province_News.html', webdir+'\Province_News_Archives_1.html')



with open(webdir+'\Province_News_Archives_1.html','r+') as n:
    line=n.readline()
    newtitle='Province News Archives'
    while line.startswith("<title>") is False:
        place=n.tell()
        line=n.readline()
    if line.startswith("<title>"):
        oldplace=place
        title=line[line.find('>')+1:line.find('<',1)]
        newline=line.replace(title,newtitle)
        rest=n.read()
    if newline != line:
        n.seek(oldplace)
        n.write(newline)
        n.write(rest)

date1=re.search('AMSSND\sNews.*?for\s([A-Z]\w\w.*?\d{4})',rest).group(1)
date1=date1.replace('Feb.','Februrary')

with open(webdir+'\Province_News_Archives.html','r+') as a:
    arcline=a.readline()
    start='Week of '
    end='</a>'
    while arcline.find('<p class="larger"><a href="Province_News_Archives_1.html">') <=0:
        arcplace=a.tell()
        arcline=a.readline()
    else:
        arc2=a.readline()
        arc3=a.readline()
        arcrest=a.read()
        olddate=arcline[arcline.find(start)+len(start):arcline.find(end)]
        newarcline=arcline.replace(olddate,date1)
        olddate2=arc2[arc2.find(start)+len(start):arc2.find(end)]
        newarc2=arc2.replace(olddate2,olddate)
        olddate3=arc3[arc3.find(start)+len(start):arc3.find(end)]
        newarc3=arc3.replace(olddate3,olddate2)
        a.seek(arcplace)
        a.write(newarcline)
        a.write(newarc2)
        a.write(newarc3)
        a.write(arcrest)