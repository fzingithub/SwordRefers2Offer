class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        只要求连续的1和0，辅助数组记录连续01的个数，相邻对答案的贡献值取其小。
        '''
        if not s:
            return 0

        count = [1]
        j = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count[j] = count[j] + 1
            else:
                count.append(1)
                j += 1

        res = 0
        for i in range(1, len(count)):
            res += min(count[i], count[i - 1])

        return res

        def countBinarySubstrings(self, s: str) -> int:
            '''
            空间优化
            '''
            pre, cur, res, prec = 0, 1, 0, s[0]
            for c in s[1:]:
                if c != prec:
                    pre, cur = cur, 1
                else:
                    cur += 1
                if cur <= pre: res += 1
                prec = c
            return res
