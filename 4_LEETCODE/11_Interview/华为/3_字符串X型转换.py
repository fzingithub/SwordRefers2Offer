s, n = input().split(',')
n = int(n)

s = list(s)
num = 0
ord = True # 正序
max_num = n//2
X = []

while s:
    temp_X = [0] * n
    if num==0:
        temp_X[0] = s.pop(0)
        if s:
            temp_X[-1] = s.pop(0)
        num += 1
        X.append(temp_X[:])
        ord = True
    elif num==max_num:
        temp_X[max_num] = s.pop(0)
        X.append(temp_X[:])
        ord = False
        num -= 1
    else:
        temp_X[num] = s.pop(0)
        if s:
            temp_X[-1-num] = s.pop(0)
        num = num + 1 if ord else num-1
        X.append(temp_X[:])

# print(X)
m,n = len(X[0]), len(X)

res = []
for i in range(m):
    for j in range(n):
        if X[j][i] != 0:
            res.append(X[j][i])

print(''.join(res))

'''
ABCDEFGHIJKMLNOPQRSTUVWXYZ,6
'''







