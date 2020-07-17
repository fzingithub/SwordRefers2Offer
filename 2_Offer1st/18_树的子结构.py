# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:35:29 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False

        if pRoot1 is not None and pRoot2 is not None:

            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HasTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True

        if pRoot1 is None:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1HasTree2(
            pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(
            pRoot1.right, pRoot2.right)
