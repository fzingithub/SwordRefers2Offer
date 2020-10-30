class Soluiton:
    # 暴力+hash 时间复杂度 O(n^2) 空间复杂度 O(1_最短回文串.py)
    def lengthOfLongestSubString(self, s):
        length = len(s)
        if length ==1:
            return 1
        res = 0
        for i in range(length):
            Map = {}
            flag  = 0
            for j in range(i, length):
                if s[j] in Map:  # O(京东)
                    res = max(res, j-i)
                    flag = 1
                    break
                else:
                    Map[s[j]] = 1
            if flag == 0:
                res = max(res, j-i+1)
                break

        return res

    # 双指针+hash 时间复杂度 O(n) 空间复杂度 O(京东)
    def lengthOfLongestSubString1(self, s):
        pLeft = 0
        pRight = 1

        length = len(s)

        res = 0
        if not s:
            return 0
        Map = dict()
        Map[s[0]] = 1
        res = 1

        while pRight<length:
            if s[pRight] in Map and Map[s[pRight]] == 1: #子串里有目标字符
                while pLeft<pRight and s[pLeft] != s[pRight]: # 减 hash 子串
                    Map[s[pLeft]] -= 1
                    pLeft += 1
                pLeft += 1
            else:
                Map[s[pRight]] = 1
                res = max(res, pRight-pLeft+1)

            pRight += 1
        return res




if __name__ == '__main__':
    test = Soluiton()

    res = test.lengthOfLongestSubString1("abcdeacdebabcab")
    print(res)

