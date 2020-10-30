# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        '''
        动态规划迭代思路
        dp[i] 1_最短回文串.py,..,i 所有的二叉搜索树

        dp[i] = \sum_{k=1_最短回文串.py}^{i} dp[k-1_最短回文串.py]dp[i-k]

        dp[0] = 1_最短回文串.py   [None]
        dp[1_最短回文串.py] = 1_最短回文串.py   [1_最短回文串.py]
        dp[2] = 2   [1_最短回文串.py, null, 2], [2, 1_最短回文串.py]
        dp[3] = 5   [1_最短回文串.py, null 1_最短回文串.py, null, 2] [1_最短回文串.py, null, 2, 1_最短回文串.py] [2, 1_最短回文串.py, 3], [3, 1_最短回文串.py, null, null, 2], [3, 2, null, 1_最短回文串.py]
        '''
        pass








    def generateTrees(self, n: int):
        '''
        递归思路:多个重复分支 指数级增长 数据规模 n<8 因此可用
        '''
        def generateTrees(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []

    def generateTrees(self, n: int):
        '''
        备忘录
        '''
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int):
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right + 1):
                left_lst = left_right(left, i - 1)
                right_lst = left_right(i + 1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret

        left_right(1, n)
        return left_right(1, n)

if __name__ == '__main__':
    test = Solution()

    res = test.generateTrees(10)

    print(res)

    def preVisit(root):
        if not root:
            print('NULL')
            return
        print(root.val)
        preVisit(root.left)
        preVisit(root.right)


    for i in res:
        preVisit(i)
        print()