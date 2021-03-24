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
while i < 1500:
    print('<contact sDisplayName="hihi" sOfficeNumber="5145" sMobilNumber="151561" sOtherNumber="564596" sAccountIndex="464" sRing="Auto" group="" photoDefault="" photoSelect="0" />')
    #print("</group>")
    i += 1
print("</group>")
print("<blacklist>")
print("</blacklist>")
print("<groupinfo>")
print('<group name="Lrving_one" Ring="Auto" />')
print("</groupinfo>")
print("</contactData>")