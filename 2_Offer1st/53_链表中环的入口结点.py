# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:06:37 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        
        pFast = pHead.next.next
        pSlow = pHead.next
        
        while pFast != pSlow and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            
        if pFast == pSlow:
            pSlow = pHead      
            while pFast != pSlow:
                pFast = pFast.next
                pSlow = pSlow.next
            return pFast
        
        return None