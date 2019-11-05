# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:46:12 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        
        if sequence == None or length == 0:
            return False
        
        root = sequence[-1]
        
        #二叉搜索树左子树小于根节点
        i = 0
        while i<length-1:
            if sequence[i]>root:
                break
            i = i + 1
            
        # 二叉搜索树左子树大于根节点  
        j = i
        while j < length-1:
            if sequence[j] < root:
                return False
            j = j + 1
        
        #判断左子树是不是二叉搜索树
        bLeft = True
        if i > 0:
            bLeft = self.VerifySquenceOfBST(sequence[:i])
            
        #判断右子树是不是二叉搜索树
        bRight = True
        if i < length-1:
            bRight = self.VerifySquenceOfBST(sequence[i:-1])
            
        return bLeft and bRight
            

test = Solution()
print (test.VerifySquenceOfBST([5,7,6,9,11,10,8]))
print (test.VerifySquenceOfBST([7,4,6,5]))