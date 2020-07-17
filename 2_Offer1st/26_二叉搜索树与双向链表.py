# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:23:19 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        pLastNodeInList = None
        arg = [pRootOfTree,pLastNodeInList]
        self.convertNode(arg)
        #pLastNodeInList 指向双向链表的尾结点
        
        #我们需要返回头结点
        pHeadOfList = arg[1]
        if pHeadOfList == None:
            return None
        while pHeadOfList.left != None:
            pHeadOfList = pHeadOfList.left
            
        return pHeadOfList
    
    #中序遍历结果   pLastNodeInList 指向双向链表的尾结点
    def convertNode(self,arg):
        if arg[0] == None:
            return
        
        pCurrent = arg[0]
        
        if pCurrent.left != None:
            arg[0] = pCurrent.left
            self.convertNode(arg)
            
        pCurrent.left = arg[1]
        if arg[1] != None:
            arg[1].right = pCurrent
        
        arg[1] = pCurrent
        
        if pCurrent.right != None:
            arg[0] = pCurrent.right
            self.convertNode(arg)
        
        
if __name__ == '__main__':
    # A = TreeNode(10)
    # B = TreeNode(6)
    # C = TreeNode(12)
    #
    # A.left = B
    # A.right = C
    #
    # test = Solution()
    #
    # D = None
    # pHeadOfList = test.Convert(A)
    #
    # if pHeadOfList:
    #    print(pHeadOfList.val)


       def spread(arg):
           ret = []
           for i in arg:
               if isinstance(i, list):
                   ret.extend(i)
               else:
                   ret.append(i)
           return ret


       def deep_flatten(lst):  # 递归展开深度列表
           result = []
           result.extend(
               spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
           return result


       deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]