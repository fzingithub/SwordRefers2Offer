n,k = map(int, input().split())
S = input()

if S:
    origin = S[0]
for i in range(1,len(S)):
    if S[i]!=origin:
        k -= 1
        if k==0:
            index = i
            break
        origin = S[i]
if k==0:
    print(''.join(list(map(str, map(lambda x:1+x, map(lambda x:-x,map(int, S[index:])))))))
else:
    print('')


'''
9 3
110001001
'''
