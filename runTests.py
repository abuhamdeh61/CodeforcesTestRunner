import subprocess
import sys
from time import sleep, time
from bs4 import BeautifulSoup
import requests

"""
make sure that you have this in cpp main function and you have the problem url as a comment in first line:
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
"""
#!!!!!!!! make sure to change this to your own path !!!!!!!!
#!!!!!!!! maek sure that you also have input and output files in the same directory !!!!!!!!
with open ("C:/Users/abedh/Desktop/C++/main.cpp") as f:
    url=f.readline()
    url=url[2:]
        
htmlPage=requests.get(url)
soup=BeautifulSoup(htmlPage.content,'html.parser')
timeLimit=soup.find('div',class_='time-limit').text


#remove all the characters except numbers
timeLimit=''.join(filter(str.isdigit, timeLimit))

soup=soup.findAll('pre')
inputs,outputs=[],[]

for i in range(len(soup)):
    soup[i]=str(soup[i]).replace('<br/>',' ')
    soup[i]=BeautifulSoup(soup[i],'html.parser')
    if i%2==0:
        inputs.append(soup[i].text)
    else:
        outputs.append(soup[i].text.strip())

for i  in range(len(outputs)):
    outputs[i]=outputs[i].replace(' ','')
    outputs[i]=outputs[i].replace('\n','')
counter=0
for input,output in zip(inputs,outputs):
    with open('input.txt','w') as f:
        f.write(input)
    
    #run the program 
    subprocess.call('g++ -o a main.cpp',shell=True)
    #calculate time with meliseconds
    time1=time()
    
    subprocess.call('a.exe',shell=True)
    
    time2=time()
    timeTaken=time2-time1
    #convert to miliseconds and round it 
    timeTaken=round(timeTaken*1000)
    timeLimit=round(int(timeLimit)*1000)
    
    if timeTaken>int(timeLimit):
        print('\033[91m'+'Time Limit Exceeded: '+str(timeTaken)+'\033[0m')
        break
    else:
        print('\033[92m'+'Time Taken: '+str(timeTaken)+'ms'+'\033[0m')
    with open('output.txt','r') as f:
        out=f.read()
        out=out.replace(' ','')
        out=out.replace('\n','')
        print(output)
        if out==output:
            print('\033[92m'+str(out)+'\033[0m')
            counter+=1
        else :
            print('\033[91m'+str(out)+'\033[0m')
        #kill the process
       
    print('---------------------------------')

if(counter==len(inputs)):
    print('\033[92m'+'Passed!'+'\033[0m')
    #print the number of test cases passed in green color
    print('\033[92m'+str(counter)+'/'+str(len(inputs))+' test passed!'+'\033[0m')
else:
    print('\033[91m'+'Failed'+'\033[0m')
    print('\033[91m'+str(counter)+'/'+str(len(inputs))+' test passed!'+'\033[0m')
