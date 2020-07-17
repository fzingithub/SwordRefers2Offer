class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pHeadOfList = None
        self.pTailOfList = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return

        self.Convert(pRootOfTree.left)

        if not self.pHeadOfList:  # 找表头
            self.pHeadOfList = pRootOfTree
            self.pTailOfList = pRootOfTree
        else:
            self.pTailOfList.right = pRootOfTree
            pRootOfTree.left = self.pTailOfList
            self.pTailOfList = pRootOfTree

        self.Convert(pRootOfTree.right)

        return self.pHeadOfList

