class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        '''
        按行打印二叉树
        :param pRoot:
        :return: List[List, List]
        '''

        if not pRoot:
            return []

        curLayer = [pRoot]
        res = []

        while curLayer:
            nextLayer = []
            resTemp = []

            for pNode in curLayer:
                resTemp.append(pNode.val)
                if pNode.left:
                    nextLayer.append(pNode.left)
                if pNode.right:
                    nextLayer.append(pNode.right)

            res.append(resTemp[:])
            curLayer = nextLayer

        return res


if __name__ == '__main__':
    test = Solution()

    Tree = TreeNode(10)
    Tree.left = TreeNode(5)
    Tree.right = TreeNode(12)

    Tree.left.left = TreeNode(4)
    Tree.left.right = TreeNode(7)

    result = test.Print(Tree)

    print(result)
