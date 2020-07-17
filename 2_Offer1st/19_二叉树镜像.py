# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:47:29 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None or (root.left == None and root.right == None):
            return
        
        root.left,root.right = root.right,root.left
        
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        