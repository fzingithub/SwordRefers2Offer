# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val<p.val and root.val<q.val:  # 当前根最小，其二值只能在右子树中
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val>p.val and root.val>q.val: # 当前根最大，其二值只能在左+子树中
            return self.lowestCommonAncestor(root.left, p, q)
        return root # 否则返回当前节点，有可能相等，可能不相等，合并输出
