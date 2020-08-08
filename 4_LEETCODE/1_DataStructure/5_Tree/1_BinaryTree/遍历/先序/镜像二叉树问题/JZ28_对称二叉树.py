# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        设置对称函数即可。
        '''

        def isImage(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                return root1.val == root2.val and (
                            isImage(root1.left, root2.right) and isImage(root1.right, root2.left))
            else:
                return False

        return isImage(root, root)
