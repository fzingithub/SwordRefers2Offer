class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # 根据树高，时间复杂度高。
    def IsBalanced(self, pRoot):
        if not pRoot:
            return True

        return abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) <= 1 and self.IsBalanced(
            pRoot.left) and self.IsBalanced(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0

        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1

    # 后序遍历解决, 时间复杂低。
    def IsBalanced_Solution(self, pRoot):
        return self.IsBalancedAndTreeDepth(pRoot) != -1

    def IsBalancedAndTreeDepth(self, pRoot):
        '''
        树平衡返回树高，树不平衡返回-1
        :param pRoot:
        :return: int
        '''
        if not pRoot:
            return 0

        leftDepth = self.IsBalancedAndTreeDepth(pRoot.left)
        if leftDepth == -1:
            return -1
        rightDepth = self.IsBalancedAndTreeDepth(pRoot.right)
        if rightDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return -1

        return max(leftDepth, rightDepth) + 1



