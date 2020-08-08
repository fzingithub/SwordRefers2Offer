# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, minNum, maxNum):
        if not root:
            return True

        if not maxNum > root.val > minNum:
            return False

        return self.helper(root.left, minNum, root.val) and self.helper(root.right, root.val, maxNum)