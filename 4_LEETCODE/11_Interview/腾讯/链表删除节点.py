k,n = map(int,input().split())

nums = list(map(int, input().split()))

nums.pop(n-1)

print(' '.join(map(str, nums)))

'''
5 3
京东 2 3 4 5
'''