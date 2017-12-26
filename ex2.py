# -*- coding: UTF-8 -*-

num = int(raw_input("输入金额："))

amt = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for i in range(0,6):
    if num>amt[i]:
        r += (num-amt[i])*rat[i]
        print (num-amt[i])*rat[i]
        num=amt[i]
print r
