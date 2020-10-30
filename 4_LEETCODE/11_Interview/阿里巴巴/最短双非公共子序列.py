a = input()
b = input()

def Count01(a):
    res = 0
    L = [False, False]
    for i in a:
        L[int(i)] = True
        if L[0] and L[1] :
            res += 1
            L[0], L[1] = False, False
    return res + 1

num1, num2 = Count01(a), Count01(b)
if num1!=num2:
    print(max(num1, num2))
elif num1>5:
    print(num1)
else:
    print(num1+1)


