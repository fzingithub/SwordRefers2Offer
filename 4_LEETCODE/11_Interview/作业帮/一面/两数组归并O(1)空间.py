a = [3,5,7,9]
b = [1,2,4,6,8]


def merge(a, b):
    len_a = len(a)
    len_b = len(b)

    a.extend([0]*len_b)

    Pa = len_a-1
    Pb = len_b-1

    P = len_a+len_b-1

    while Pa>=0 and Pb>=0:
        if a[Pa]>b[Pb]:
            a[P] = a[Pa]
            Pa -= 1
        else:
            a[P] = b[Pb]
            Pb -= 1
        P -= 1

    if Pb>=0:
        while Pb>=0:
            a[P] = b[Pb]
            P-=1
            Pb-=1

    return a

res = merge(a,b)

print(res)

