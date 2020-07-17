

     # -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:30:33 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#方法一 调用库函数
#from itertools import permutations
#class Solution(object):
#    def permute(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
#        return list(permutations(nums))

class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if len(ss) < 2:
            return ss.split()
        for i in range(len(ss)):
            for n in map(lambda x: x+ ss[i], self.Permutation(ss[:i]+ss[i+1:])):
                if n not in res:
                    res.append(n)
        return sorted(res)


if __name__ == '__main__':
    test = Solution()
    
    res = test.Permutation('abcdv')
            