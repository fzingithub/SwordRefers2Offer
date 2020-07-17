# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:25:25 2019

@author: zhe
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#方法一， 中序全排序， 找第k的。
class Solution1:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0: return None
        res = []
        self.inOrder(pRoot, res)
        if len(res) < k:
            return None
        return res[k - 1]

    def inOrder(self, root, res):
        if not root: return
        if root.left:
            self.inOrder(root.left, res)
        res.append(root)
        if root.right:
            self.inOrder(root.right, res)



#方法二， 节省时间 不全排序。
#1. 递归左子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。 
#2. 当左子树没有返回节点时，判断当前的根节点是不是第k个遍历到的值（即第k大）。如果是，则返回该节点，停止递归。 
#3. 当左子树和根节点都没有返回节点时，递归右子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。

class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or self.count >= k:
            return None
        node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return pRoot
        node = self.KthNode(pRoot.right, k)
        if node:
            return node
        
if  __name__ == '__main__':
    test = Solution()

    Tree = TreeNode(5)
    Tree.left = TreeNode(3)
    Tree.right = TreeNode(7) 
    
    Tree.left.left = TreeNode(2)
    Tree.left.right = TreeNode(4)
    Tree.right.left = TreeNode(6)


    result = test.KthNode(Tree, 4)
    print (result.val , test.count)
    result1 = test.KthNode(Tree, 4)
    print(test.count)
    result2 = test.KthNode(Tree, 4)
    print(test.count)

