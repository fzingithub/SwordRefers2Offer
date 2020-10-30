
T = int(input())

for _  in range(T):
    m,n = map(int, input().split())
    if m%2==1 and n%2==1 and min(m,n)!=1:
        print(min(m,n))
        continue
    else:
        print(2)



