# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:17:09 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#解法一：冒泡思想 O(n^2) O(1)
class Solution:
    def InversePairs(self, data):
        # write code here
        num = 0
        for i in range(len(data)-1,0,-1):
            flag = False
            for j in range(i):
                if data[j]>data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]
                    num = num + 1
                    flag = True
                
            if not flag:
                break
                
        return num%1000000007
    
    
#解法二：归并思想 O(nlogn) O(n)   空间换取时间
import math
class Solution1:
    def InversePairs(self, data):
        if not data :
            return False
        if len(data)==1 :
            return 0
        def merge(tuple_before,tuple_after):
            array_before = tuple_before[0]
            cnt_before = tuple_before[1]
            array_after = tuple_after[0]
            cnt_after = tuple_after[1]
            cnt = cnt_before+cnt_after
            flag = len(array_after)-1
            array_merge = []
            for i in range(len(array_before)-1,-1,-1):
                while array_before[i]<=array_after[flag] and flag>=0 :
                    array_merge.append(array_after[flag])
                    flag -= 1
                if flag == -1 :
                    break
                else:
                    array_merge.append(array_before[i])
                    cnt += (flag+1)
            if flag == -1 :
                for j in range(i,-1,-1):
                    array_merge.append(array_before[j])
            else:
                for j in range(flag ,-1,-1):
                    array_merge.append(array_after[j])
            return array_merge[::-1],cnt

        def mergesort(array):
            if len(array)==1:
                return (array,0)
            cut = math.floor(len(array)/2)
            tuple_before=mergesort(array[:cut])
            tuple_after=mergesort(array[cut:])
            return merge(tuple_before, tuple_after)

        return mergesort(data)[1]%1000000007


class Solution2:
    def InversePairs(self, data):
        # write code here
        if not data:
            return False
        _, res = self.mergeSort(data)
        return res % 1000000007

    def mergeSort(self, data):
        '''
        para：
            data: 待排统计逆序对序列
        return：
            (OrderedData， NumOfInversePair) ：(有序列， 逆序对数)
        '''

        length = len(data)
        if length == 1:  # 递归出口
            return (data, 0)
        middle = length // 2
        tupleLeft = self.mergeSort(data[:middle])
        tupleRight = self.mergeSort(data[middle:])
        return self.merge(tupleLeft, tupleRight)

    def merge(self, tupleLeft, tupleRight):
        '''
        para:
            tupleLeft: 左半有序数据列表以及其逆序数组成的元组
            tupleRight: 右半有序数据列表以及其逆序数组成的元组
        return:
            (OrderedData， NumOfInversePair): (合并的有序数据列表， 总的逆序对数)
        '''

        # 参数解析
        dataLeft = tupleLeft[0]
        dataRight = tupleRight[0]
        numLeft = tupleLeft[1]
        numRight = tupleRight[1]
        num = numLeft + numRight

        data = []
        while dataLeft and dataRight:
            if dataRight[0] < dataLeft[0]:
                num += len(dataLeft)
                data.append(dataRight.pop(0))
            else:
                data.append(dataLeft.pop(0))

        data.extend(dataLeft) if dataLeft else data.extend(dataRight)

        return data, num
        
if __name__=='__main__':
    test = Solution2()
    res = test.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575])

    print (res)
            