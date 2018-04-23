#!/usr/bin/python
# -*- coding: UTF-8 -*-
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict

# 删除键是name的条目
del dict['Name']
print dict

# 清空词典所有的条目
dict.clear()
print dict

# 删除词典
del dict
print dict['Age']

# 不允许同一个键出现两次。
# 创建时如果同一个键被赋值两次，后一个值会被记住
