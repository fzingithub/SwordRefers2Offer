# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:17:30 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = {}
        
        for ele in s:
            dic[ele] = 1 if ele not in dic else dic[ele]+1
            
        for num in range(len(s)):
            if dic[s[num]] == 1:
                return num
        return -1
        
if __name__ == '__main__':
    test = Solution()
    
    result = test.FirstNotRepeatingChar('qq')
    