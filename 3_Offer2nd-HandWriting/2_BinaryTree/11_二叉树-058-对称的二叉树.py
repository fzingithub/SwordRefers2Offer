class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        return self.isMirror(pRoot, pRoot)

    #判断两棵树是否互为镜像二叉树
    def isMirror(self, pRoot1, pRoot2):
        if pRoot1 and pRoot2 and pRoot1.val == pRoot2.val:
            return self.isMirror(pRoot1.left, pRoot2.right) and self.isMirror(pRoot1.right, pRoot2.left)
        elif not pRoot1 and not pRoot2:
            return True
        else:
            return False