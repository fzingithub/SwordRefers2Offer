n = int(input())
point = list(map(int, input().strip().split()))
a = []
for i in range(n):
    b = list(input())
    a.append(b[:])
start = [[point[0], point[1]]]
gox = [1,0,-1,0]
goy = [0,1,0,-1]
dp = [[-1] * n for _ in range(n)]
dp[point[0]][point[1]] = 0
while len(start):
    cur = start.pop(0)
    if cur[0] == point[2] and cur[1] == point[3]:
        break
    for i in range(4):
        cur_x = cur[0] + gox[i]
        cur_y = cur[1] + goy[i]
        if cur_x>=0 and cur_x<n and cur_y>=0 and cur_y<n and a[cur_x][cur_y]!='#' and a[cur_x][cur_y]!='@' and (dp[cur_x][cur_y]>(dp[cur[0]][cur[1]]+1) or dp[cur_x][cur_y]==-1):
            dp[cur_x][cur_y] = dp[cur[0]][cur[1]] + 1
            start.append([cur_x,cur_y])
print(dp[point[2]][point[3]])