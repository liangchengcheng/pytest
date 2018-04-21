#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = "Hello"
b = "Python"

print "a + b 的结果是 ", a + b
print "a * 2 的结果是 ", a * 2
print "a[1] 的结果是 ", a[1]
print "a[1:4] 的结果是 ", a[1:4]

if ("H" in a):
    print "H 在 a中"
else:
    print "H 不在a中"

if ("M" not in a):
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"

print r'\n'
print R'\n'
print "My name is %s and weight is %d kg!" % ('Zara', 21)
