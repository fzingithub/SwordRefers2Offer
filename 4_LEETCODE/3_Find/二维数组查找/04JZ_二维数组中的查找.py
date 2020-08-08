class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False
        i, j = 0, len(matrix[0]) - 1
        iLength = len(matrix)
        while i < iLength and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False

if __name__ == '__main__':
    test = Solution()
    matrix = [[1,4,7,11,15],
              [2,5,8,12,19],
              [3,6,9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 5
    res = test.findNumberIn2DArray(matrix, target)

    print(res)