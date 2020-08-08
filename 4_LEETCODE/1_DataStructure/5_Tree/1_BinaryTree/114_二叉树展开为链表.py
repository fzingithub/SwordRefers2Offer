class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

if __name__ == '__main__':
    test = Solution()
    pList = [0] * 10

    for i in range(10):
        pList[i] = TreeNode(i)

    index = 0
    i = 0
    while index <= 7:
        pList[i].left = pList[index + 1]
        pList[i].right = pList[index + 2]
        i += 1
        index += 2

    root = pList[0]

    test.flatten(root)


    while root:
        print(root.val)
        root = root.right


