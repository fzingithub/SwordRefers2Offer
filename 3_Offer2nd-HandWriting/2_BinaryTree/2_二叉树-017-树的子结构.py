class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        '''
        树2是否是树1的子结构，根节点数据域不必相等
        :param pRoot1:
        :param pRoot2:
        :return: Bool
        '''
        if not pRoot1  or not pRoot2:
            return False

        if not self.DoesTree1HasTree2(pRoot1, pRoot2):
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return True



    def DoesTree1HasTree2(self, pRoot1, pRoot2):
        '''
        树1的包含树2 树1从根节点开始包含
        :param pRoot1:
        :param pRoot2:
        :return: Bool
        '''

        if not pRoot2:
            return True
        elif pRoot1 and pRoot2 and pRoot1.val == pRoot2.val:
            return self.DoesTree1HasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right, pRoot2.right)
        else:
            return False

