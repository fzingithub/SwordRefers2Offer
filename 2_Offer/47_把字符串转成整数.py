# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:32:02 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def StrToInt(self, s):
        res,mult,flag = 0,1,1
        if not s:
            return res
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = -1
            s = s[1:]
        for i in range(len(s)-1, -1, -1):
            if '9' >= s[i] >= '0':
                res += (ord(s[i]) - 48)*mult
                mult = mult * 10
            else:
                return 0
        return res*flag

if __name__ == '__main__':
    test = Solution()
    res = test.StrToInt('-45891')