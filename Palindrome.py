# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:13:20 2020

@author: marko
"""


p_phrase = "was it a car or a cat I saw"

count = len(p_phrase)

r_phrase = ""

for word in p_phrase:
    r_phrase = r_phrase + p_phrase[count-1]
    
    count -= 1
    
print(r_phrase)
    
    



