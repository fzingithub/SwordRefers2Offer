class TrieNode(object):
    def __init__(self):
        # 是否构成一个完成的单词
        self.is_word = False
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        """Add a string to this trie."""
        p = self.root
        n = len(s)
        for i in range(n):
            if p.children[ord(s[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_word = True
                p.children[ord(s[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(s[i]) - ord('a')]
                if i == n - 1:
                    p.is_word = True
                    return

    def search(self, s):
        """Judge whether s is in this trie."""

        p = self.root
        for c in s:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False


class Solution:
    def respace(self, dictionary, sentence):
        '''
        方法：2_DP+字典树
        字典树：3_Trie 是一种最大程度利用多个字符串前缀信息的数据结构，它可以在 O(w) 的时间复杂度内判断一个字符串是否是一个字符串集合中某个字符串的前缀，其中 w 代表字符串的长度。

        动态规划:
        状态定义：dp[i]:  前 i 个字符最少的未识别的字符数量。
        状态转移：不管找没找到
                dp[i] = dp[i-1]+1
                考虑从第j(j<=i)个到第i个组成的子串sentence[j-1, ..., i-1](索引是从零开始的)能否在dict中找到。
                dp[i] = min(dp[i], dp[j-1])

        边界：dp[0] = 0
        res = dp[-1]

        时间复杂度 O(n^2 + |dict|) = O(n^2)
        空间复杂度 O(|dict|∗S+n)

        :param dictionary:  字典
        :param sentence:    未分割的句子
        :return:
        '''

        m = len(sentence)

        dp = [0] * (m+1)

        dp[0] = 0

        trie = Trie()

        for word in dictionary:
            trie.add(word[::-1])



        for i in range(1, m+1):
            dp[i] = dp[i-1] + 1

            pTrieNode = trie.root

            for j in range(i, 0, -1):
                pNextNode = pTrieNode.children[ord(sentence[j-1]) - ord('a')]
                if pNextNode:
                    if pNextNode.is_word:
                        dp[i] = min(dp[i], dp[j-1])

                    pTrieNode = pNextNode
                else:
                    break
        return dp[m]












if __name__ == '__main__':
    test = Solution()

    res = test.respace(["looked","just","like","her","brother"],"jesslookedjustliketimherbrother")

    print(res)