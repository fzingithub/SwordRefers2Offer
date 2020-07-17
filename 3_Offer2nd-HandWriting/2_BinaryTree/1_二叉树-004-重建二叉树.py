class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    '''
    不含重复数字的前序遍历以及中序遍历重建二叉树
    '''
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None

        rootVal = pre[0]
        pNode = TreeNode(rootVal)
        indexSpl = tin.index(rootVal)
        pNode.left = self.reConstructBinaryTree(pre[1:1+indexSpl], tin[:indexSpl])
        pNode.right = self.reConstructBinaryTree(pre[1+indexSpl:], tin[indexSpl+1:])

        return pNode


