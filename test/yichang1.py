#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile","w")
    try:
        fh.write("这是一个测试文件，用于测试异常")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "error 没有找到文件，或者文件读取异常"