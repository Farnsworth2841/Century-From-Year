# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 00:51:04 2018

@author: danie
"""

def century(year):
    # Finish this :)
    if year <= 100:
        return 1
    elif year < 1000:
        if str(year)[-2:] != 0o1:
            return int(str(year)[:1]) + 1
    if year >= 1000:
        if int(str(year)[-2:]) == 00:
            return int(str(year)[:2])            
    elif str(year)[-2:] != 0o1:
        return int(str(year)[:2]) + 1

