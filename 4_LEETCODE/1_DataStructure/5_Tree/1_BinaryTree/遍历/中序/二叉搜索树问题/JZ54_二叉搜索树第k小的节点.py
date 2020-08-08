# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        res = []

        def midOrderTravesal(root):
            if not root:
                return None

            midOrderTravesal(root.left)
            res.append(root.val)
            midOrderTravesal(root.right)

        midOrderTravesal(root)

        return res[-k]
