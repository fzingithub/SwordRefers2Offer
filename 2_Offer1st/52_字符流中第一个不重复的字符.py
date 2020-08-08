# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:26:45 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
# python3 dict 虽说无序， 但实为假有序。
class Solution:
    # 返回对应char
    charDict = {}
    def FirstAppearingOnce(self):
        # write code here
        for key in self.charDict:
            if self.charDict[key] == 1:
                return key
        return '#'
        
    def Insert(self, char):
        # write code here
        self.charDict[char] = 1 if char not in self.charDict else self.charDict[char]+1
        
        
# python2 dict 全无序
class Solution1:
    # 返回对应char
    charDict = {}
    s = ""
    def FirstAppearingOnce(self):
        for key in self.s:
            if self.charDict[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        self.charDict[char] = 1 if char not in self.charDict else self.charDict[char]+1
        self.s += char

        
if __name__ == '__main__':
    s = 'google'
    test = Solution1()
    for i in s:
        test.Insert(i)
        print (test.FirstAppearingOnce())
        
