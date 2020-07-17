class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1]) if s.strip() else s

    # 注意使用切片反转 返回反转后的列表
    # 使用str.reverse() 函数原地翻转 无返回值