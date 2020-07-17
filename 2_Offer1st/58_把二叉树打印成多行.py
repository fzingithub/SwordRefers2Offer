# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:06:11 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        
        resultList = []
        currLayer = [pRoot]
        
        #层次遍历的变种
        while currLayer:
            currList = []
            nextLayer = []
            
            #层遍历
            for node in currLayer:
                currList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
                    
            resultList.append(currList)
            currLayer = nextLayer
            
        return resultList
            
            