class Solution:
    def moveStoneMinNum(self, data):
        '''
        分析：保持原来数组中最长递增子序列不变，移动其他石子，再用序列长度减去最长子序列个数即得答案。

        dp[i] 是以 A[i-1]为尾的最长序列数长度。

        dp[i] = max(dp[j-1] + 1) if data[i-1]==data[j]+1 j=0,1,...,i-2

        dp[0] = 0
        dp[1] = 1
        res = max(dp)

        T:O(n^2)
        M:O(n)
        '''
        n = len(data)

        dp = [1] *(n+1)

        for i in range(2,n+1):
            for j in range(i-1):
                if data[i-1]==data[j]+1:
                    dp[i] = max(dp[j+1]+1, dp[i])

        return n-max(dp)

    def moveStoneMinNum(self, data):
        '''
        hash
        最好 O(n)
        最坏 O(n^2)
        '''
        if not data:
            return 0

        AList_map = []
        for num in data:
            flag = 0
            if AList_map:
                for map_old in AList_map:
                    if num-1 in map_old:
                        flag = 1
                        map_old[num] = 1
            if flag==0:
                map_new = {}
                map_new[num] = 1
                AList_map.append(map_new)

        res = max(map(len, AList_map))

        return len(data)-res




if __name__== '__main__':
    test = Solution()
    data = [1,11,12,2,16,3,13,4,14,5,15,6,17,18,7,19,8,20,9,10]
    res = test.moveStoneMinNum(data)

    print(res)
