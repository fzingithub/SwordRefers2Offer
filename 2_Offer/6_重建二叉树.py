# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:25:58 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None

        rootVal = pre[0]  # 结点真值
        rootNode = TreeNode(rootVal)  # 创建结点
        separateIndex = tin.index(rootVal)  # 相对分割点索引
        rootNode.left = self.reConstructBinaryTree(pre[1:separateIndex + 1], tin[:separateIndex])
        rootNode.right = self.reConstructBinaryTree(pre[separateIndex + 1:], tin[separateIndex + 1:])

        return rootNode
        