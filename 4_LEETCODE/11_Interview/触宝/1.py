A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

for i in range(len(A2)):
    temp = 1
    ob = A2[i]
    while ob in A1:
        if temp > 1:
            A2.insert(i, ob)
        A1.pop(A1.index(ob))
        temp += 1
    if temp==1:
        A2.pop(i)

A1.sort()
print(A2+A1)


'''
京东 2 3 4 5 6 7
3 6 5
12 45
23
京东 2 2 3
3 2
'''
