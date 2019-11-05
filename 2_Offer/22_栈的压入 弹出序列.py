# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:40:55 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here  
        
        if len(pushV) != 0 and len(pushV) != 0:
            pushV.reverse()
            popV.reverse()  
            
            stack = [] 
            
            while True:
                
                while popV[-1] not in stack:
                    if pushV:
                        stack.append(pushV.pop())
#                    else:
                        return False  
                    
                if popV[-1] == stack[-1]:
                    popV.pop()
                    stack.pop()
                else:
                    return False  
                
                if len(popV) == 0:
                    return True
                

test = Solution()


L1 = [1,2,3,4,5]
L2 = [4,5,3,2,1]
L3 = [4,3,5,1,2]

print (test.IsPopOrder(L1,L2))
#print (test.IsPopOrder(L1,L3))
                