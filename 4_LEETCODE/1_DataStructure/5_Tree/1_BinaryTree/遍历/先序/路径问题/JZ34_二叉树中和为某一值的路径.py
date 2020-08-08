class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def FindPath(self,  pRoot, expectNumber):
        if not pRoot:
            return []

        res = []
        path = []

        self.find(pRoot, expectNumber, res, path)

        return res


    def find(self, pRoot, expectNumber, res, path):
        if not pRoot:
            return

        path.append(pRoot.val)
        isLeaf = not pRoot.left and not pRoot.right

        if isLeaf and expectNumber == pRoot.val:
            res.append(path[:])

        if not isLeaf:
            self.find(pRoot.left, expectNumber-pRoot.val, res,  path)
            self.find(pRoot.right, expectNumber-pRoot.val, res,  path)

        path.pop()

# class Solution:
#     def __init__(self):
#         self.res = []
#         self.tempRes = []
#
#     def FindPath(self, pRoot, k):
#         if not pRoot:
#             return self.res
#
#         self.find(pRoot, k)
#         return self.res
#
#     def find(self, pRoot, k):
#         if not pRoot:
#             return
#         isLeaf = not pRoot.left and not pRoot.right
#
#         self.tempRes.append(pRoot.val)
#
#         if isLeaf and k == pRoot.val:
#             self.res.append(self.tempRes[:])
#
#         if not isLeaf:
#             self.find(pRoot.left, k-pRoot.val)
#             self.find(pRoot.right, k-pRoot.val)
#
#         self.tempRes.pop()



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


    res =  test.FindPath(root, 12)
    print(res)