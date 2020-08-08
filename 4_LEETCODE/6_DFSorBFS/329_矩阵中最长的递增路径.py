from functools import lru_cache


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreaseingPath(self, matrix):
        '''
        方法一：dfs+备忘录+python lru_cache decorator
        '''
        if not matrix:
            return 0

        @lru_cache(None)  # maxsize=128
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


    def longestIncreaseingPath(self, matrix):
        '''
        方法一：dfs+备忘录
        '''
        if not matrix:
            return 0

        memo = dict()
        def dfs(row, col)->int:
            if (row, col) in memo:
                return memo[(row, col)]
            best = 1
            for x, y in Solution.DIRS:
                newRow, newCol = x+row, y+col
                if 0<=newRow<rows and 0<=newCol<cols and matrix[newRow][newCol]>matrix[row][col]:
                    best = max(best, dfs(newRow, newCol)+1)

            memo[(row, col)] = best
            return best
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))

        return res



if __name__ == '__main__':
    test = Solution()

    matrix = [
             [9,9,4],
             [6,6,8],
             [2,1,1]
             ]
    import time
    start = time.time()
    res = test.longestIncreaseingPath(matrix)
    end = time.time()
    print(res,end-start)

