import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import csv

data=[]

def extract_content(url):
     r = requests.get(url)
     soup = BeautifulSoup(r.content,'lxml')
     tag_list= OrderedDict()
     
     tag_list={
        "LINK Text":"a",
        "H1 Heading Text":"h1",
        "H2 Heading Text":"h2",
        "DIV Container Text":"div",
        "UL Text":"ul",
        "Label Text":"label",
        "SPAN Text":"span",
        "Table Text":"table",
        "Paragraph Text":"p" 
        }

     for i,(tag_name,search_tag) in enumerate(tag_list.items()):
         for element in soup.find_all(search_tag):
             if element is not None:
                 string=""
                 if (element.text is not None) and (element.text is not string.strip()):
                     line=element.text
                     line = line.replace('\n','')
                     
                     data.append(tag_name+"@--@"+line)
                     print(tag_name+"@--@"+line)
                
          
     return data
                    
    



def main(url):
    #Get All the data and extract 
  
    for finalData in extract_content(url):
        data2=finalData.split("@--@")
        #print(data2[0])
        try:
          f=open('data.csv','a')
          f.write(data2[0]+"------->>>>>>>----"+data2[1]+"\n")
        except Exception as e:
            print(e)

        

 





main('http://www.example.com')

