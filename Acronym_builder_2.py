# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:30:57 2020

@author: marko
"""


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

sent_list = sent.split(" ")

acro = ""

for word in sent_list:
    
    if word not in stopwords:
        
        acro = acro + word[0].upper() + word[1].upper()+ ". "
        
acro = acro[:-2]   
  
print(acro)