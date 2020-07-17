class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sumNum):
        '''
        先序
        '''
        if not root:
            return False
        if not root.left and not root.right:
            return sumNum == root.val

        sumvalue = sumNum - root.val
        return self.hasPathSum(root.left, sumvalue) or self.hasPathSum(root.right, sumvalue)

if __name__ == '__main__':
    test = Solution()
    pList = [0]*10

    for i in range(10):
        pList[i] = TreeNode(i)

    index = 0
    i = 0
    while  index<=7:
        pList[i].left = pList[index+1]
        pList[i].right = pList[index+2]
        i += 1
        index += 2

    root = pList[0]


    res =  test.hasPathSum(root, 12)
    print(res)