# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:43:03 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        while listNode is not None:
            result.append(listNode.val)
            listNode = listNode.next
        result.reverse()
        return result