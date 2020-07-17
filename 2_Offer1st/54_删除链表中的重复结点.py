# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:52:24 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                while curr and curr.val==val:
                    curr = curr.next
                last.next = curr
        return first.next
                    
        
        
        
        