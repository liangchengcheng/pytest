#!/usr/bin/python
# -*- coding: UTF-8 -*-

def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print b  # 结果是 2


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），
# 传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，
# 只是修改另一个复制的对象，不会影响 a 本身。




#可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），
# 则是将 la 真正的传过去，修改后fun外部的la也会受影响


# 可写函数说明 可变参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)