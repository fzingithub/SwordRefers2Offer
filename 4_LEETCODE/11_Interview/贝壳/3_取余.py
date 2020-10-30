a, b = list(map(int, input().split()))
if a==b:
    print('inf')
elif a>b:
    res = 0
    if a%2==0:
        if b>=a//2:
            print(0)
        else:
            for i in range(1, a-b+1):
                if a%i==b:
                    res+=1
            print(res)
    if a%2!=0:
        if b>a//2:
            print(0)
        else:
            for i in range(1, a-b+1):
                if a%i==b:
                    res+=1
            print(res)
else:
    print(0)

# 6
# 10 2
# 11 13
# 23 6
# 45 7
# 34 8
# 12 京东
