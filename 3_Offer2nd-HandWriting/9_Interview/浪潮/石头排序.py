
'''
分析：保持原来数组中最长递增子序列不变，移动其他石子，再用序列长度减去最长子序列个数即得答案。

dp[i] 是以 A[i-1]为尾的最长序列数长度。

dp[i] = max(dp[j-1] + 1) if data[i-1]==data[j]+1 j=0,1,...,i-2

dp[0] = 0
dp[1] = 1
res = max(dp)
'''
data  = [4,1,2,5,3]
n = len(data)
dp = [0] *(n+1)

for i in range(2,n+1):
    for j in range(i-1):
        if data[i-1]==data[j]+1:
            dp[i] = max(dp[i-1]+1, dp[i])
        else:
            dp[i] = 1

print(n-max(dp))