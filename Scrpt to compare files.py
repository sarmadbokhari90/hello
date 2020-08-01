import os
import re
path = ''
mylist0=[]
mylist1=[]
files=[]
for file in os.listdir(path):
    if not file.startswith('.'):
        files.append(file)i=0
for file in files:
    with open((path+file),'r') as f:
        text= f.read()
        match=re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',text)
    
    mylist0.append(match)
    i+=1
getsubnet=False
for val in mylist0[0]:
    if getsubnet == True: 
        mylist1.append((val)+'\n')
        getsubnet=False
    elif val not in mylist0[1]:
        mylist1.append(val)
        getsubnet=True
    
print (' '.join(map(str,mylist1)))
 