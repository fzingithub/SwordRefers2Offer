class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        '''
        树的深度等于左右子树高的加一
        :param pRoot:
        :return: int
        '''

        if not pRoot:
            return 0

        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1