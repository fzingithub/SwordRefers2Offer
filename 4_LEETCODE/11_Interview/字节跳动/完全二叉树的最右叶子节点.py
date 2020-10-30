class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def lastOneNodeOfCBT(self, pRoot):
        '''
        往左右子树的树高的方向查询， 一样高往右查询 O(logn)

        全完二叉树的树高 向左遍历即可。 O(logn)

        时间复杂度 O((logn)^2) 优于层次遍历 O(n)
        '''

        if pRoot and not pRoot.left:
            return pRoot

        def getHighOFCBT(pNode):
            nums = 0

            while pNode:
                nums += 1
                pNode = pNode.left
            return nums

        leftHigh = getHighOFCBT(pRoot.left)
        rightHigh = getHighOFCBT(pRoot.right)

        if rightHigh == leftHigh:
            pNode = self.lastOneNodeOfCBT(pRoot.right)
        else:
            pNode = self.lastOneNodeOfCBT(pRoot.left)

        return pNode

if __name__ == '__main__':
    test = Solution()

    m = 10
    pList = [TreeNode(i) for i in range(m)]

    i = 0
    j = 1
    pRoot = pList[0]
    pNode = pRoot
    while j<m:
        pList[i].left = pList[j]
        j += 1
        if j==m:
            break
        pList[i].right = pList[j]
        j += 1
        i += 1

    # while pNode:
    #     print(pNode.val)
    #     pNode = pNode.right

    def PBTree(pNode):
        if not pNode:
            return

        print(pNode.val)
        PBTree(pNode.left)
        PBTree(pNode.right)

    PBTree(pRoot)

    print(test.lastOneNodeOfCBT(pRoot).val)