#importing the libraries
import pandas as shortpanda
import numpy as shortnum
import re
import datetime
from collections import Counter
from bs4 import BeautifulSoup
#reading CSV Data
QuestionData =shortpanda.read_csv('Questions.csv',encoding='latin-1')
TagsData=shortpanda.read_csv('Tags.csv')
#creating a list of Tags from TagsData
Taglist=TagsData.Tag.tolist()
#creating a list of Tags from TagsData
SortedTaglist=Counter(Taglist)
print(SortedTaglist) #analyzing whether the Data is sorted or not
list(QuestionData)
CreationDateList=QuestionData.CreationDate.tolist()
print(CreationDateList)

#finding the week number
Week= datetime.date(2014,4,17).isocalendar()[1]

#counting the number of most frequent word in Title Data

Titlelist=QuestionData.Title.tolist()

print(Titlelist)


with open('TitleData.txt') as titlefile:
    TitleRead=titlefile.read()
    Words = re.findall(r'\w+', TitleRead)
   
    WordCount = Counter(Words)
    

#Cleaning Data by removing HTML Tags ,Links and Code Snippets
   
    Bodylist=QuestionData.Body.tolist() # list of unproceesed question data
#Using BeautifulSoup for Noise Removal
    
    #for cleaning HTML headers
   
    def HTML_ClEAN(text):
        TrimData=BeautifulSoup(text,'html.parser')
        return TrimData.get_text
        
   # for removing  unnecessary code snippets, ,links, URL...
    def remove_CodeSnippet(text):
      
        return re.sub('<pre><code>.*?</code></pre>', '', text)
   
    def remove_Para(text):
      
        return re.sub('</p>\\n\\n<p>', '', text)
    
    with open('BodyData.txt') as Datafile:
        DataRead=Datafile.read()
        
        HTML_ClEAN(DataRead)
        remove_CodeSnippet(DataRead)
        remove_Para(DataRead)
     
      



      
        
    
    
  
    




