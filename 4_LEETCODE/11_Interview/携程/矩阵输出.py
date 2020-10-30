row, col = map(int, input().split())

num = 1

mat = [[0] * col for _ in range(row)]
for i in range(row+col-1):
    for j in range(i,-1,-1):
        try:
            mat[j][i-j] = num
            num += 1
        except:
            pass
print(mat)

