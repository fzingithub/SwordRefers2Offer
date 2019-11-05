# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:39:49 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#求二叉树的深度
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        
        return max(nLeft+1,nRight+1)