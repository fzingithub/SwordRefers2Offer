# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 08:49:02 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # print binary tree from top to  bottom
    def PrintFromTopToBottom(self, root):
        queue = []
        result = []
        if root == None:
            return result

        queue.append(root)
        while queue:
            newNode = queue.pop(0)
            result.append(newNode.val)
            if newNode.left != None:
                queue.append(newNode.left)
            if newNode.right != None:
                queue.append(newNode.right)
        return result
    
    # print binary tree to multiple line
    def PrintMultLine(self, pRoot):
        if not pRoot:
            return []
        resultList = []
        curLayer = [pRoot]
        while curLayer:
            curList = []
            nextLayer = []
            for node in curLayer:
                curList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            resultList.append(curList)
            curLayer = nextLayer
            
        return resultList
    
    # print binary tree in 'z' mode.
    def Print(self, pRoot):
        resultArray = []
        if not pRoot:
            return resultArray
        curLayerNodes = [pRoot]
        isEvenLayer = True
        while curLayerNodes:
            curLayerValues = []
            nextLayerNodes = []
            isEvenLayer = not isEvenLayer
            for node in curLayerNodes:
                curLayerValues.append(node.val)
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            resultArray.append(curLayerValues[::-1]) if isEvenLayer else resultArray.append(curLayerValues)
        return resultArray
        
        