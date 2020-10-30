# import sys
# sys.setrecursionlimit(10000) #10000为设置的栈大小

s = int(input())
a = list(map(int, input().split(" ")))
m, n = a[0], a[1]
b = []
for i in range(m):
    c = list(map(int, input().split(" ")))
    b.append(c[:])
path = [[False] * n for _ in range(m)]
def dfs(b, i, j,path):
    if i<0 or i>=m or j<0 or j>=n or path[i][j] or b[i][j]==0:
        return False
    if i==m-1 and j==n-1:
        return True
    path[i][j] = True
    return dfs(b, i+s, j,path) or dfs(b, i-s, j,path) or dfs(b, i, j+s,path) or dfs(b, i, j-s,path)

bools = dfs(b, 0, 0,path)
if bools:
    print(1)
else:
    print(0)

'''
京东
5 5
京东 京东 京东 京东 京东
0 0 0 0 京东
京东 京东 京东 京东 京东
京东 0 0 0 0
京东 京东 京东 京东 京东
京东
5 5
京东 0 京东 京东 京东
京东 0 京东 0 京东
京东 0 京东 0 京东
京东 0 京东 0 京东
京东 京东 京东 0 京东
'''