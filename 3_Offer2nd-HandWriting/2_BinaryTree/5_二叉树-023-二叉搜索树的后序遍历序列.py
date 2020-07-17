class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 题目要求初始为空时，输出为False，与递归出口不相符。单拎出来一个递归函数即可。
        if not sequence:
            return False

        return self.recursionFun(sequence)

    def recursionFun(self, sequence):
        if not sequence:
            return True

        length = len(sequence)
        pRootVal = sequence[-1]

        for i in range(length):
            if sequence[i]>pRootVal:
                break
        # 此时切分元素是 i
        for j in range(i, length):
            if sequence[j]<pRootVal:
                return False

        return self.recursionFun(sequence[:i]) and self.recursionFun(sequence[i:-1])

if __name__ == '__main__':
    test = Solution()
    res = test.VerifySquenceOfBST([])
    print(res)