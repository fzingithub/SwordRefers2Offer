# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:29:57 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#方法一：全排列做法
import itertools
class Solution1:
    def PrintMinNumber(self, numbers):
        # write code here
        '''
        1_最短回文串.py、首先 numbers 是一个 set 集合,需要将其转换为 列表进行排序    sorted(list(data)))
        2、然后通过python的内置库 itertools.permutations   进行排列组合
        3、将排列组合出来的数先转为字符串
        4、然后通过 join 将其组合成一个字符串
        5、将组合出的数字字符串加入新的 set 集合中
        '''
        fullAS = list(itertools.permutations(numbers))
        fullA = []
        
        for i in fullAS:
            resTemp = ''
            for s in i:
                resTemp = resTemp + s 
            fullA.append(int(resTemp))     
        
        return min(fullA)
        
class Solution2:
    def theMax(self, str1, str2):
        '''
        定义字符串比较函数：
        所以在这里自定义一个比较大小的函数，比较两个字符串s1, s2大小的时候，先将它们拼接起来，
        比较s1+s2,和s2+s1那个大，如果s1+s2大，那说明s2应该放前面，所以按这个规则，
        s2就应该排在s1前面。
        '''
        return str1 if str1+str2 > str2+str1 else str2

    def PrintMinNumber(self, numbers):
        """使用冒泡进行排序(把最大的放最后)"""
        string = [str(num) for num in numbers]
        flag = True
        count = len(string) - 1
        while flag and  count > 0:
            flag = False
            for i in range(len(string)-1):
                if self.theMax(string[i], string[i+1]) == string[i]:
                    temp = string[i]
                    del string[i]
                    string.insert(i+1, temp)
                    flag = True
            count -= 1
        string = ''.join(string)
        return string



#精简方法二
class Solution3:
    def PrintMinNumber(self, numbers):
        # write code here
        from functools import cmp_to_key    #将cmp转成key值  [-1_最短回文串.py,0,1_最短回文串.py]
        if not numbers: return ""
        numbers = list(map(str, numbers))
        numbers.sort(key=cmp_to_key(lambda x,y: int(x+y)-int(y+x))) #key=[-1_最短回文串.py,0,1_最短回文串.py]
        return "".join(numbers).lstrip('0') or '0'   #join 字符串用 ’‘ 连接函数 ；lstrip 移去串首的空白字符     
    
if __name__ == '__main__':
    test = Solution3()
    
    res = test.PrintMinNumber(['03','032','321','4','3','32','321','4''3','32','321','4','3','32','321','4'])