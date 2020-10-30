class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        '''
        方法一
        '''
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

    def printMatrix(self, matrix):
        '''
        方法二
        '''
        # write code here
        if matrix == None:
            return None

        try:
            row = len(matrix)
            col = len(matrix[0])
        except:
            return []

        if row <= 0 or col <= 0:
            return

        result = []
        start = 0
        while start * 2 < row and start * 2 < col:
            self.PrintMatrixInCicle(matrix, start, result, row, col)
            start += 1

        return result

    def PrintMatrixInCicle(self, matrix, start, result, row, col):
        endX = col - 1 - start
        endY = row - 1 - start
        # 从左到右
        j = start
        while j <= endX:
            result.append(matrix[start][j])
            j += 1

        # 从上到下
        i = start + 1
        while i <= endY:
            result.append(matrix[i][endX])
            i += 1

        if endX == start or endY == start:
            return
        # 从右到左
        j = endX - 1
        while j >= start:
            result.append(matrix[endY][j])
            j -= 1

        # 从下到上
        i = endY - 1
        while i >= start + 1:
            result.append(matrix[i][start])
            i -= 1


if __name__ == '__main__':
    test = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    res = test.spiralOrder(matrix)

    print(res)

    # matrix = [[京东, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # res = test.printMatrix(matrix)
    #
    # print(res)