nums = list(map(int, input().split(',')))
right = {5:1, 10:1, 20:1}

has = []
flag = False

for i in range(len(nums)):
    if nums[i] in right:
        if nums[i] == 5:
            has.append(5)
        elif nums[i] == 10:
            if 5 in has:
                has.pop(has.index(5))
                has.append(10)
            else:
                res = 'false,'+str(i+1)
                print(res,end='')
                flag = True
                break
        else:
            if 5 in has and 10 in has:
                has.pop(has.index(5))
                has.pop(has.index(10))
                has.append(10)
            elif has.count(5)>=3:
                has.pop(has.index(5))
                has.pop(has.index(5))
                has.pop(has.index(5))
            else:
                res = 'false,' + str(i + 1)
                print(res, end='')
                flag = True
                break
    else:
        res = 'false,' + str(i + 1)
        print(res, end='')
        flag = True
        break
if not flag:
    res = 'true,'+str(len(nums))
    print(res,end='')
