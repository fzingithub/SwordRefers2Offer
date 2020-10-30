T = int(input())

nums = []
for _ in range(T):
    nums.append(int(input()))

def split(num):
    a = num//2
    b = num - a
    return sum(map(int, list(str(a)))) + sum(map(int, list(str(b))))

for num in nums:
    print(split(num))

'''
京东
35
'''