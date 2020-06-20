# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.tempRes = []
        self.res = []
        self.n = 0

    def backtrack(self, k):
        if k >= self.n:
            self.res.append(''.join(self.tempRes))
        else:
            for i in range(k, self.n):
                self.tempRes[k], self.tempRes[i] = self.tempRes[i], self.tempRes[k]
                
                if k<1 or self.tempRes[k][0] >= self.tempRes[k-1][-1]:
                    self.backtrack(k + 1)
                elif self.tempRes[k][0] < self.tempRes[k-1][-1]:
                    self.res.append(''.join(self.tempRes[:k]))

                self.tempRes[k], self.tempRes[i] = self.tempRes[i], self.tempRes[k]

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.tempRes = list(ss)
        self.n = len(ss)
        self.backtrack(0)

        return max(map(len,self.res))

if __name__ == '__main__':
    test = Solution()

    res = test.Permutation(['aaa','aab', 'abcd','aaaaaaaa'])

    print(res)