n = int(input())

nums_list = []
for _ in range(n):
    nums = list(map(int, input().split()))


    if nums[0] == 1:
        nums_list.insert(nums[1]-1, nums[2])
    elif nums[0] == 2:
        nums_list.pop(nums[1]-1)
    else:
        print(' '.join(list(map(str, nums_list))))

'''
3
1 1 3
1 2 4
3
'''