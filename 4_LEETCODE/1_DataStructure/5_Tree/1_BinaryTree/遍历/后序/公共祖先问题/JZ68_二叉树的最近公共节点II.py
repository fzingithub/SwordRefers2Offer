# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root is p or root is q:  # 若为空反空， 若等于其中一个返回该节点。+
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 左子树中存不存在目标节点之一。
        right = self.lowestCommonAncestor(root.right, p, q)  # 右子树中存不存在目标节点之一。
        if not left:  # 若左子树中没有，则两节点一定在右子树中，返回后序遍历的后位节点。
            return right
        elif not right:  # 若右子树中没有，则两节点一定在左子树中，返回后序遍历的后位节点。
            return left
        else:  # 否则一定分别在左右子树之中， 返回当前根节点。
            return root