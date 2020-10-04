# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:15:37 2020

@author: marko
"""


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores_list = scores.split(" ")

print(scores_list)

a_scores = 0

for score in scores_list:
    if int(score) >= 90:
        a_scores += 1
        
print(a_scores)