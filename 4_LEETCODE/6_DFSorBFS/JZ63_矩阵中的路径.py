# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:17:51 2019

@author: zhe
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        if not board and word:
            return False

        rows, cols = len(board), len(board[0])
        assistMat = [[True] * cols for _ in range(rows)]

        def find(path, row, col):
            if not path:
                return True

            if 0 <= row < rows and 0 <= col < cols and assistMat[row][col] and board[row][col] == path[0]:
                assistMat[row][col] = False
                if find(path[1:], row - 1, col) or find(path[1:], row + 1, col) or find(path[1:], row, col - 1) or find(
                        path[1:], row, col + 1):
                    return True

                assistMat[row][col] = True
            else:
                return False

        for row in range(rows):
            for col in range(cols):
                if find(word, row, col):
                    return True

        return False
        
           