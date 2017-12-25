# -*- coding: UTF-8 -*-

num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and i!=k):
                print str(num)+':'+str(i)+str(j)+str(k)
                num = num+1
print num
