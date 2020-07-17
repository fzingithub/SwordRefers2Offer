class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # 中序遍历的下一个节点
    def GetNext(self, pNode):
        if not pNode:
            return None

        if pNode.right: # 存在右子树
            pNodeleft = pNode.right
            while pNodeleft.left:  #找右子树的最左节点
                pNodeleft = pNodeleft.left
            return pNodeleft
        else: # 不存在右子树
            while pNode.next and pNode.next.left is not pNode:
                pNode = pNode.next

            return pNode.next