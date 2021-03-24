#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving


from urllib import request

url = 'https://maoyan.com/films'

rq = request.Request(url)

resp = request.urlopen(url)
print(resp.read().decode('utf-8'))