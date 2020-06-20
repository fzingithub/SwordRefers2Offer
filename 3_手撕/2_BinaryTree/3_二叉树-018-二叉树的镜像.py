class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, pRoot):
        '''
        原地反转
        :param pRoot:
        :return:  pRoot
        '''
        if not pRoot:
            return None

        pRoot.left, pRoot.right = self.Mirror(pRoot.right), self.Mirror(pRoot.left)

        return pRoot
