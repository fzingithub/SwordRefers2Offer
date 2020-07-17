# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:42:40 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        
        pAhead = head
        pbehind = head
        
        i=1
        while i < k :
            if pAhead.next != None:
                pAhead = pAhead.next
                i = i + 1
            else:
                return None
        
        while pAhead.next != None:
            pAhead = pAhead.next
            pbehind = pbehind.next
        
        return pbehind
            
                    
            
        