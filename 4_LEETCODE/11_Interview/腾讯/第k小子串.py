s = input()
k = int(input())

strs = set(s[i:i+x+1] for x in range(len(s)) for i in range(len(s)-x))
strs = list(strs)
strs.sort()

print(strs[k-1])


'''
aabb
3
'''