s, n = map(int, input().split())

distances = [0]*n
times = [0]*n
for i in range(n):
    distances[i], times[i] = map(int, input().split())

flag = False
for sp in range(s, -1, -1):
    temp = False
    for j in range(n):
        if ((distances[j]/(sp/3.6))//times[j])%2 == 1:# 不通过
            temp = True
            break

    if not temp:
        print(sp)
        flag = True
        break

if not flag:
    print(0)

'''
50 京东
200 15
50 京东
200 10
'''