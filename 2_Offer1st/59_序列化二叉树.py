aca't# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:27:47 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。需要注意的是，
#序列化二叉树的过程中，如果遇到空节点，需要以某种符号（这里用#）表示。以下图二叉树为例，
#序列化二叉树时，需要将空节点也存入字符串中。

#反序列化二叉树：根据某种遍历顺序得到的序列化字符串，重构二叉树。具体思路是
#按前序遍历“根左右”的顺序，根节点位于其左右子节点的前面，即非空（#）的第一个节点
#是某子树的根节点，左右子节点在该根节点后，以空节点#为分隔符。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)
    
    
    def Deserialize(self, s):
        # write code here
        listS = s.split(',')
        return self.deserialize(listS)
    
    def deserialize(self, listS):
        if len(listS) <= 0:
            return None
        
        value = listS.pop(0)
        root = None
        if value != '#':
            root = TreeNode(int(value))
            root.left = self.deserialize(listS)
            root.right = self.deserialize(listS)
        return root
    
    
if  __name__ == '__main__':
    test = Solution()
    
    Tree = TreeNode(10)
    Tree.left = TreeNode(5)
    Tree.right = TreeNode(12)
    
    Tree.left.left = TreeNode(4)
    Tree.left.right = TreeNode(7)
    Tree.right.left = TreeNode(6)
    
    resultS = test.Serialize(Tree)
    
    resultD = test.Deserialize(resultS)