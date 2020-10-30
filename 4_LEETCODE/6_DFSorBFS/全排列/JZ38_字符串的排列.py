class Solution:
    def permutation(self, s: str) -> 'List[str]':
        c, res = list(s), []
        length = len(c)
        def dfs(x):
            if x==length-1:
                res.append(''.join(c))
                return
            dic = set()
            for i in range(x, length):
                if c[i] in dic: continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x+1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res

if __name__ == '__main__':
    test = Solution()
    s = 'aab'
    '''
    a a b
      a   a(剪枝) b
     a b         a a(剪枝)
    b   a       a
    
    aab, aba, baa
    '''
    res = test.permutation(s)
    print(res)