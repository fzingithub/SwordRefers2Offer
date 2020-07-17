# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:54:11 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

s = ' hello world '
 
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return "%20".join(s.split(" "))
#        return s.replace(' ','%20')        #It's OK!

        
if __name__ == '__main__':
    sol = Solution()
    print(s.split(' '))
    print (sol.replaceSpace(s))
    
    
#python 中的 str 对象是不可变类型 ， 不可能实现 在原有字符串内存空间上操作。
#因此 无论从前往后 还是从后往前 将不会极大的改变其时间复杂度。