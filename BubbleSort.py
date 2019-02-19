#!/usr/bin/env python
# encoding: utf-8
"""
@Company：华中科技大学电气学院
@version: V1.0
@author: Victor
@contact: 1650996069@qq.com 2018--2020
@software: PyCharm
@file: BubbleSort.py
@time: 2019/2/19 9:53
@Desc：冒泡排序法：从第一个元素开始，比较相邻两个元素的大小，若大小有误，则对调，然后进行下一对元素的比较
                 如此扫描一遍之后，便可以确保最后一个元素排序是对的，接着进行第二次扫描，直到所有排序都是正确的。

                 n个元素需要扫描的最少次数为n-1次
"""
import datetime
startime = datetime.datetime.now()

data = [12,45,2,47,90,23,67,34,1]#len=9
print("冒泡排序：原始数据为：")
for i in range(len(data)):
    print("%3d"%data[i],end='')
print(' ')

for p in range(len(data)):

    for j in range(1,len(data)-p):
        if data[j-1] < data[j]:
            data[j-1],data[j] = data[j],data[j-1]

    print("第%d次扫描后的结果："%(p+1),end='')
    for k in range(len(data)):
        print('%3d' % data[k],end='')
    # if (p >= 1) and dic[p] == dic[p-1]:
    #     break

print("排序后的结果：")
print(data)


endtime = datetime.datetime.now()
print((endtime-startime).microseconds)
