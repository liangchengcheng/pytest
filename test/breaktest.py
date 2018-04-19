#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':
    if letter == 'h':
        break
    print '当前的字母:', letter

var = 10
while var > 0:
    print '当前的变量值为', var
    var = var - 1
    if var == 5:
        break
print "---程序结束---"