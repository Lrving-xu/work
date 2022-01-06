#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @autor Lrving

import csv

csvFile=open("C:/Users/Lrving/Desktop/test.csv",'w', newline='')
writer=csv.writer(csvFile)
writer.writerow(["数据集名称","mac","ip","model"])
for i in range(1, 100):
    writer.writerow(((("数据集-{:0>1d}".format(i))),

                     (("001fc1{:0>6d}".format(i))),

                     (("10.3.2.{:0>1d}".format(i))),

                     (('UC926U'))

                     ))

csvFile.close()