# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:38:28 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#不考虑时间复杂度的做法 暴力搜素  O(nlogn)
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        for i in range(1,n+1):
            res = res + self.NumberOf1(i)
            
        return res
    
    def NumberOf1(self,n):
        res = 0
        
        while n!=0:
            if n%10 == 1:
                res = res +1
            n = n//10
        return res
    

#考虑数字特性 O(logn)
class Solution2:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        """
        :type n: int
        :rtype: int
 
        例：对于824883294，先求0－800000000之间（不包括800000000）的，再求0－24883294之间的。
        如果等于1，如1244444，先求0－1000000之间，再求1000000－1244444，那么只需要加上244444＋1，再求0－244444之间的1
        如果大于1，例：0－800000000之间1的个数为8个100000000的1的个数加上100000000，因为从1000000000－200000000共有1000000000个数且最高位都为1。
        对于最后一位数，如果大于1，直接加上1即可。
        """
        result = 0
        if n < 0:
            return 0
        length = len(str(n))
        listN = list(str(n))
        for i, v in enumerate(listN):
            a = length - i - 1  # a为10的幂
            if i==length-1 and int(v)>=1:
                result+=1
                break
 
            if int(v) > 1:
                result += int(10 ** a * a / 10) * int(v) + 10**a
            if int(v) == 1:
                result += (int(10 ** a * a / 10) + int("".join(listN[i+1:])) + 1)
        return result
        
if __name__ == '__main__':
    test = Solution2()
    
    result = test.NumberOf1Between1AndN_Solution(123456789)