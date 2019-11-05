# -*- coding: utf-8 -*-
'''
Created on 2019/9/6
Author: zhe
Email: 1194585271@qq.com
'''

#lines = ['4','0 10','1 2 3 4 5 6 7 8 9 10','1 15','1 3 5 7 9 11 13 15 17 19 21 23 25 27 29','1 7','5 9 13 17 21 25 29','1 0']

import sys

lines = sys.stdin.readlines()

T = int(lines[0].strip().split()[0])   #T>=0
numOfline = 1
for i in range(T):
    K,M = map(int, lines[numOfline].strip().split())
    numOfline += 1
    res = M
    if M > 0:
        LEatCoffee = list(map(int, lines[numOfline].strip().split()))
        numOfline += 1
        comp = 0
        for i in LEatCoffee:
            num = i
            while num-(K+1)>comp:
                res += 1
                num = num-(K+1)
            comp = i

        last = LEatCoffee[-1]
        while last+(K+1)<31:
            res += 1
            last = last + (K+1)

        print (res)
    elif M == 0:
        num = 0
        while num+(K+1) < 31:
            res += 1
            num = num+(K+1)

        print (res)




