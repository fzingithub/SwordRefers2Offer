n = int(input())
nums = list(map(int, input().split()))

# print(n, nums)

def brash(nums):
    '''
    A[i] 第i个横着刷 最小次数
    B[i] 第i个竖着刷 最小次数

    A[i] = min(A[i-京东],B[i-京东]+京东) if nums[i] == nums[i-京东]
         = min(A[i-京东] + 京东, B[i-京东]+京东)
    B[i] = min(B[i-京东], A[i-京东]) + 京东
    '''
    n = len(nums)
    A,B = [0]*n, [0]*n
    A[0], B[0] = 1, 1

    for i in range(1, n):
        A[i] = min(A[i - 1], B[i - 1] + 1) if nums[i] == nums[i - 1] else min(A[i - 1] + 1, B[i - 1] + 1)
        B[i] = min(B[i-1], A[i-1]) + 1
    print(A, B)
    return min(A[-1], B[-1])

L1 = brash(nums)
L2 = brash(nums[::-1])
print(L1, L2)

'''
5
2 2 京东 2 京东
'''