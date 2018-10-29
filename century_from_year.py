# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 00:51:04 2018

@author: danie
"""

def century(year):
    ##Function that when given a year, will return the century it is in
    #make sure that we have a number
    numbah = int(year)
    #year 12124
    if numbah >= 1001:
        test_number = 1000
        while numbah > test_number:
            test_number += 100
        if numbah <= test_number:
            century =  str(test_number)[-4:-2]
    if numbah <=1000:
        test_number = 0
        while numbah > test_number:
            test_number += 100
        if numbah <= test_number:
            century = str(test_number)[0]
    #adding the specific century words
    list_of_words = ['st Century', "nd Century", "rd Century", "th Century"]
    if century[-1] == str(1):
        return str(century) + list_of_words[0]
    elif century[-1] == str(2):
        return  str(century) + list_of_words[1]
    elif century[-1] == str(3):
        return  str(century) + list_of_words[2]
    else:
        return str(century) + list_of_words[-1]
   
    

