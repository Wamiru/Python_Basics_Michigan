# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:21:56 2020

@author: marko
"""


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

org_list = org.split(" ")

acro = ""

for word in org_list:
    
    if word not in stopwords:
        
        acro = acro + word[0].upper()
        
print(acro)

