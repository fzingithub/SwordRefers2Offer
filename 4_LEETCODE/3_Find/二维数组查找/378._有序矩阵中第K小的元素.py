class Solution:

    # 内置排序 时间复杂度O(nlogn) 空间O(n)
    def kthSmallest(self, matrix, k):
        return sorted(sum(matrix, []))[k - 1]



    # 插入排序 时间O(n^3) 空间O(nm)
    def KthSmallest1(self, List, k):
        data = []

        for i in List:
            length = len(i)
            pleft = 0
            while data and data[-1] > i[pleft]:
                dataIndex = len(data) - 1
                while i[pleft] < data[dataIndex] and dataIndex >= 0:
                    dataIndex -= 1
                data.insert(dataIndex + 1, i[pleft])
                pleft += 1

            data.extend(i[pleft:])

        return data[k - 1]

    # 归并排序 O(n^2logn) 归并O(n)
    def KthSmallest2(self, matrix, k):

        data = []
        for i in matrix:
            data = self.merge(data, i)

        return data[k-1]


    def merge(self, L1, L2):

        res = []
        while L1 and L2:
            res.append(L1.pop(0)) if L1[0] < L2[0] else res.append(L2.pop(0))

        res.extend(L1) if not L2 else res.extend(L2)
        return res



    # 小顶堆 heapq
    def kthSmallest3(self, matrix, k):
        import heapq
        n = len(matrix)
        m = len(matrix[0])

        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1 and y<m-1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]

    # 二分查找
    def kthSmallest4(self, matrix, k) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    test = Solution()
    matrix = [
                 [1, 5, 9],
                 [10, 11, 13],
                 [12, 13, 15],
             ]
    k = 8

    res = test.kthSmallest(
        matrix,
        k
    )

    print(res)