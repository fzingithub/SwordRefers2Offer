n = int(input())

total = 2*n-1
grid = [[0]*total for _ in range(n)]
dp = [[0]*(2*n+1) for _ in range(n+1)]

for i in range(n):
    nums = list(map(int, input().strip().split()))
    k = 0
    for j in range(total//2-i, total//2+i+1):
        grid[i][j] = nums[k]
        k += 1

for i in range(1, n+1):
    for j in range(1, n+3):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + grid[i-1][j-1]

print(max(dp[-1]))







'''
4
     1
   2 1 2
 3 4 2 1 3
3 4 6 2 3 4 1

3
     1
   2 1 2
 3 4 2 1 3
dp[i][j] 代表走到i-1，j-1处 最大收益
dp[i][j] = dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j + 1]) + grid[i - 1][j - 1]
'''