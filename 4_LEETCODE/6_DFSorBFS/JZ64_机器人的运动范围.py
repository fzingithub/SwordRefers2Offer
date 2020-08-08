# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:15:14 2019

@author: zhe
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        rows, cols = m, n
        AssistMat = [[True] * n for _ in range(m)]

        def find(row, col):
            def judge(row, col):
                return sum(map(int, str(row)+str(col))) <= k

            count = 0
            if 0 <= row < rows and 0 <= col < cols and judge(row, col) and AssistMat[row][col]:
                AssistMat[row][col] = False
                count = 1 + find(row + 1, col) + find(row - 1, col) + find(row, col - 1) + find(row, col + 1)

            return count

        return find(0, 0)
    
    
    
if __name__ == '__main__':
    test = Solution()
    res = test.movingCount(75,45,10)

    print(res)