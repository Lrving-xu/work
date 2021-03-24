#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving


import random
import sys



output=sys.stdout
outputfile=open('phonebook.xml','w' ,encoding='utf-8')
sys.stdout=outputfile

print('<?xml version="1.0" encoding="UTF-8"?>')
print("<contactData>")
print("<group>")
i = 0
while i < 20:
    list_one = ['a', 'A', 'B','b','C','c']
    list_two= ['a', 'A', 'B','b','C','c']
    list_three= ['a', 'A', 'B','b','C','c']
    name = random.choice(list_one)+random.choice(list_two)+random.choice(list_three)
    number_one = random.randint(13000000000,13999999999)
    number_two = random.randint(13100000000,13999999999)
    number_three = random.randint(13200000000,13999999999)
    number_four = random.randint(13300000000,13999999999)
    print('<contact sDisplayName="%s" sOfficeNumber="%d" sMobilNumber="%d" sOtherNumber="%d" sAccountIndex="%d" sRing="Auto" group="" photoDefault="" photoSelect="0" />' %(name,number_one, number_two,number_three,number_four ))
    i += 1
print("</group>")
print("<blacklist>")
print("</blacklist>")
print("<groupinfo>")
print('<group name="Lrving_one" Ring="Auto" />')
print("</groupinfo>")
print("</contactData>")



# name = "lrving"
# number = 21515
# print('<contact sDisplayName="%s" sOfficeNumber="%d"/>'%(name,number))