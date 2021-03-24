#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving

import random
import sys

output=sys.stdout
outputfile=open('phonebook.xml','w' ,encoding='utf-8')
sys.stdout=outputfile

# book_file = open('phonebook.xml', mode='w',encoding='utf-8')
print('<?xml version="1.0" encoding="UTF-8"?>')
print("<PhoneDirectory>")
i = 0
# list_one = ['a', 'A', 'B','b','C','c']
# list_two= ['a', 'A', 'B','b','C','c']
# list_three= ['a', 'A', 'B','b','C','c']
# name = random.choice(list_one)+random.choice(list_two)+random.choice(list_three)
# phone_number = random.randint(13000000000,13999999999)

while i <= 19:
    list_one = ['a', 'A', 'B','b','C','c']
    list_two= ['a', 'A', 'B','b','C','c']
    list_three= ['a', 'A', 'B','b','C','c']
    name = random.choice(list_one)+random.choice(list_two)+random.choice(list_three)
    phone_number = random.randint(13000000000,13999999999)


    print("<DirectoryEntry>")
    print("<Name>%s</Name>" %name)
    print("<Telephone>%d</Telephone>" % phone_number)
    print("</DirectoryEntry>")

    #print("</PhoneDirectory>")
    i = i+1
print("</PhoneDirectory>")
outputfile.close()
sys.stdout=output