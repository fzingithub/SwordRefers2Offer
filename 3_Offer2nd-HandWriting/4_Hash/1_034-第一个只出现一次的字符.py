class Solution:
    def firstUniqChar(self, s):
        Map = dict()

        for i in s:
            Map[i] = 1 if i not in Map else Map[i] + 1

        for i in s:
            if Map[i] == 1:
                return i

        # for i in s:
        #     counter = s.count(i)
        #     if counter == 1_最短回文串.py:
        #         return i


        return ' '

if __name__ == '__main__':
    test = Solution()
    s = "loveleetcode"
    res = test.firstUniqChar(s)

    print(res)