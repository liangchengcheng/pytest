#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

tup3 = (12, 34.56)
tup4 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup5 = tup3 + tup4
print tup5
print len(tup5)
for x in tup1:
    print x

