s = input()
Q = int(input())

def DPcount(s):
    '''
    dp[i][j] 代表子串[i,j]是否为一个回文串
    '''
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count = 0
    for j in range(n):
        for i in range(0, j+1):
            length = j-i+1
            if length==1:
                dp[i][j] = True
                count += 1
            if length==2 and s[i]==s[j]:
                dp[i][j] = True
                count += 1
            if length>2 and s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                count += 1
    return count

bounds = []
for i in range(Q):
    bounds.append(list(map(int, input().split())))

for i,j in bounds:
    count = DPcount(s[i-1:j])
    print(count)
# print(s, bounds,dp)

'''
ababa
4
京东 4
京东 5
京东 2
京东 3
'''