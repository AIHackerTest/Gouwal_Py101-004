# -*- coding: utf-8 -*-
weather = {}
history = {}

with open('C:\\Users\\CNNEZHA2\\mystuff\\Py104\\Py101-004\\Chap1\\project\\weather_info.txt', 'r', encoding = 'utf-8' ) as f:
    for line in f:
        key, value = line.split(',')
        weather[key] = value
print("%s" % weather)
