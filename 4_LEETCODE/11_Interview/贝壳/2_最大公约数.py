

T = int(input())


def gcd(m, n):
    '''
    辗转相除 对数级的时间复杂度
    '''
    if m < n:
        m, n = n, m
    while n:
        temp = m % n
        m, n = n, temp
    return m

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))

    n = len(data)
    flag = 0
    for i in range(n):
        for j in range(i, n):
            if gcd(i,j)==1:
                flag = 1
                print(0)
        if flag == 1:
            break

