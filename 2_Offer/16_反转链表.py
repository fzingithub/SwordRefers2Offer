# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:35:10 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
         
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        
        pleft = pHead
        pmiddle = pHead.next
        pright = pmiddle.next
        
        pHead.next = None
        while True:
            pmiddle.next = pleft
            if pright == None:
                break
            else:
                pleft = pmiddle
                pmiddle = pright
                pright = pright.next
        return pmiddle
        
        