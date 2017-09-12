# Chap1 Task1
#-*-coding:utf-8 -*-
import csv
import collections
reader = {}
weather = {}
dr = {}

for f in files:
    filename = (f['':','])
with open('C:\\Users\\CNNEZHA2\\mystuff\\py104\\py101-004\\chap1\\project\\weather_info.txt', newline='', encoding = 'utf-8') as csvfile:

#    fieldnames = ['city_name',]
    reader = csv.DictReader(csvfile, delimiter = ' ')

    dr = [(csvfile, i['city'],i['weather']) for i in dr]

    print("%s" % dr)
