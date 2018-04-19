#!/usr/bin/python
# -*- coding: UTF-8 -*-

numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
i = 1
while i < 10:
    i +=1
    if i %2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break

