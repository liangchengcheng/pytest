#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 重命名
os.rename("test1.txt", "test2.txt")

# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")

# 创建目录test
os.mkdir("test")

# 给出当前的目录
print os.getcwd()

# 删除”/tmp/test”目录
os.rmdir( "/tmp/test"  )