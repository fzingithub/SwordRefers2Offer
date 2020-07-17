# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:23:52 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split()[::-1]) if s.strip() != "" else s

if __name__ == '__main__':
    test = Solution()
    res = test.ReverseSentence('i am a student. ')