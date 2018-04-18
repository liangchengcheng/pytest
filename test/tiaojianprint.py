#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 例子 1 if的基本用法
flag = False
name = 'lunrn'
if name == 'python':
    flag = True
    print  'welcom boss'
else:
    print name
num = 5
if num == 3:
    print 'boss'
elif num == 2:
    print "user"
elif num == 1:
    print "worker"
elif num < 0:
    print 'error'
else:
    print 'random'

number = 9
if number >= 0 and number <= 10:
    print 'hello'
else:
    print 'undefine'

number = 8
if (number >= 0 and number <= 5) or (number >= 10 and number <= 15):
    print  '你好啊'
else:
    print 'undefine'
