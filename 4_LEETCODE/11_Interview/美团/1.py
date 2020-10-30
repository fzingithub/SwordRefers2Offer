m = int(input())


res_n = 0
res = []
for i in range(2178,m+1):
    reverse_num = int(''.join(list(str(i))[::-1]))
    if i*4==reverse_num:
        res_n += 1
        res.append(str(i)+' '+str(reverse_num))


print(res_n)
for i in res:
    print(i)


