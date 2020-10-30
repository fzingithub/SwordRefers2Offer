class Solution:
    def shortestPalindrome_front(self, s: str) -> str:
        '''
        暴力+串后加
        '''
        if s=='':
            return ''
        ss=s[::-1]
        for i in range(len(s)):
            length=len(s)-i
            if ss[i:]==s[:length]:
                return ss+s[length:]

    def shortestPalindrome_behind(self, s: str) -> str:
        '''
        暴力+串前加
        '''
        if s=='':
            return ''
        ss=s[::-1]
        for i in range(len(s)):
            length=len(s)-i
            if s[i:]==ss[:length]:
                return s+ss[length:]

    def shortestPalindrome_advanced(self, s: str) -> str:
        '''
        KMP 算法
        '''
        def get_table(p):
            table = [0] * len(p)
            i = 1
            j = 0
            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = get_table(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s

if __name__ == '__main__':
    test = Solution()
    s = 'abcac'

    res = test.shortestPalindrome_behind(s)
    print(res)
