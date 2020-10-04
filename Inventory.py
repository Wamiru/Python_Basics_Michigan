# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:47:44 2020

@author: marko
"""


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    
    item_list = item.split(", ")
    
    print("The store has {} {}, each for {} USD.".format(item_list[1],item_list[0],item_list[2]))