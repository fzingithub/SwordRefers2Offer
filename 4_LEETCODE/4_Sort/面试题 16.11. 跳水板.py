class Solution:
    def divingBoard(self, shorter, longer, k):
        '''
        暴力 O(k^2) O(m)
        '''
        res = []
        if k == 0:
            return []

        for i in range(0, k + 1):
            for j in range(0, k + 1):
                if i + j == k:
                    res.append(shorter * i + longer * j)

        return sorted(res)


    def divingBoard(self, shorter, longer, k):
        '''
        小的从大到小取
        '''

        if k==0:
            return []
        res = []

        if shorter==longer:
            return [shorter*k]

        for i in range(k, -1, -1):
            res.append(i*shorter+(k-i)*longer)

        return res





if __name__ == '__main__':
    test = Solution()

    res = test.divingBoard(1, 2, 3)

    print(res)