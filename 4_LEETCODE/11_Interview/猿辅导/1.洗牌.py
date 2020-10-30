N,M = map(int, input().split())
digs = list(map(int, input().split()))


array = digs+[-1]*N
print(array)
results = [None] * (2 * N)
for j in range(2 * N):
    index = j
    for i in range(M):
        index = 2 * index
        if index >= 2 * N:
            index = index % (2 * N) + 1
    results[index] = array[j]
n, k = digs[-2:]
results = map(str, results)
print(' '.join(results))


'''
6 2 
1 2 6 3 4 5
'''