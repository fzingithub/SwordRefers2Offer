# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:43:04 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1_最短回文串.py,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            currentNode = queue.pop(0)
            result.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        
        return result