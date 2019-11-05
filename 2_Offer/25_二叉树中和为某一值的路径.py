# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:04:47 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        
        res = [] #返回的结果二维列表
        path = [] #路径列表
        
        self.find(root,expectNumber,res,path)
        
        return res
    
    def find(self,root,expectNumber,res,path):
        if not root:
            return
        
        path.append(root.val) #记录路径信息
        
        isLeaf = not (root.left or root.right)#判断是否为叶子结点
        
        if isLeaf and expectNumber == root.val:#满足要求添加到结果列表
            res.append(path.copy()) #注意必须用顶层copy
            
        if root.left:#递归左子树
            self.find(root.left,expectNumber-root.val,res,path)
            
        if root.right:#递归右子树
            self.find(root.right,expectNumber-root.val,res,path)        
        
        path.pop()
        
        return 
        

if  __name__ == '__main__':
    test = Solution()
    
    Tree = TreeNode(10)
    Tree.left = TreeNode(5)
    Tree.right = TreeNode(12)
    
    Tree.left.left = TreeNode(4)
    Tree.left.right = TreeNode(7)
    
    result = test.FindPath(Tree,22)
        