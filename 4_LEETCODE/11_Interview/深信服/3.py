T = int(input())

for _ in range(T):
    n = int(input())
    leftNums = [0]*n
    rightNums = [0]*n
    for i in range(n):
        leftNums[i], rightNums[i] = map(int, input().split())

    minNum = min(leftNums)
    maxNum = max(rightNums)

    res = 0
    for i in range(minNum, maxNum+1):
        temp = 0
        for j in range(n):
            if leftNums[j]<=i<=rightNums[j]:
                temp+=1
        res = max(res, temp)
    print(res)




'''
3
2
2 5
8 9
3
4 10
7 12
10 10
10
2 8
9 10
4 7
2 5
5 7
3 6
京东 4
6 9
7 8
4 6

'''