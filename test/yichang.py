#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    fh = open("testfile",'w')
    fh.write("这是一个测试文件，用来测试异常")
except IOError:
    print "没有找到文件或者读取文件失败"
else:
    print "内容写入成功"
    fh.close()
try:
    fn = open("testfile","w")
    fn.write("这是一个测试文件，用来测试异常")
finally:
    print "即使有error  也会执行"