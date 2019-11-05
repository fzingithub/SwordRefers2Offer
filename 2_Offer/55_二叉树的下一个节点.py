# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:37:05 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        
        #suppose the node has right son nodes.
        if pNode.right:
            rightTreeNode = pNode.right
            while rightTreeNode.left:
                rightTreeNode = rightTreeNode.left
            return rightTreeNode
        
        #the node has no right son nodes.
        else:
            #To find it is its parent node's left node. or None
            while pNode.next and pNode != pNode.next.left:
                pNode = pNode.next
            return pNode.next