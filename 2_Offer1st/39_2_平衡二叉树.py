# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:01:53 2019

@author: zhe

E-mail: 1194585271@qq.com
"""


#判断是否为平衡二叉树

#方法一： 借鉴求二叉树的深度 但需要重复遍历  自上而下  先序遍历
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
    
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        
        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)
        
        diff = nLeft-nRight
        if diff < -1 or diff > 1:
            return False
        
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    
#方法二： 优化 不要重复遍历  自下而上  后序遍历
class Solution1:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.IsBalance(pRoot) != -1
    
    def IsBalance(self,pRoot):
        if not pRoot:
            return 0
        
        nLeft = self.IsBalance(pRoot.left)
        if nLeft == -1:
            return -1
        nRight = self.IsBalance(pRoot.right)
        if nRight == -1:
            return -1
        
        diff = nLeft - nRight
        if diff > 1 or diff < -1:
            return -1
        
        return max(nLeft,nRight)+1
        
        
    