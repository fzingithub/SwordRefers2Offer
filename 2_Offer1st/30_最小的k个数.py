# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:22:17 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#Solution1 ： 利用 python 内置排序算法 timsort 平均时间复杂度 nlogn 
class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput==None or tinput==[] or k<=0 or k>len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
    
    
#Solution2 ： 平均时间复杂度 O(n) quicksort Partition 解决 topk 问题
class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput==None or tinput==[] or k<=0 or k>len(tinput):
            return []
        
        start = 0
        end = len(tinput)-1
        index = self.Partition(tinput,start,end)
        
        while index != k-1:
            if index<k-1:
                start = index + 1
                index = self.Partition(tinput,start,end)
                
            else:
                end = index - 1
                index = self.Partition(tinput,start,end)

        return tinput[:k]
        
    
    
    def Partition(self,tinput,begin,end):
        left = begin
        right = end 
        key = tinput[begin]
        
        while left<right:
            while tinput[left]<=key and left<end:
                left = left + 1
                
            while tinput[right]>key and right>begin:
                right = right - 1
                
            if left<right:
                tinput[left],tinput[right] =tinput[right],tinput[left]
                
        tinput[begin],tinput[right] = tinput[right],tinput[begin]
        
        return right
    
    
#Solution3 ：O(nlogk) 算法，特别适合处理海量数据 小顶堆
import heapq

#大顶堆  要实现小顶堆
class TopkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []
 
    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)
 
    def TopK(self):
        #如果是大顶堆 去掉负号 正常 push
        #小顶堆 如下加上负号    push 相反数
        return [-x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])] 


class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput==None or tinput==[] or k<=0 or k>len(tinput):
            return []
        
        minHeap = TopkHeap(k)
        for i in tinput:
            minHeap.Push(-i)
        
        return minHeap.TopK()
        
    
    
if __name__ == '__main__':
    test = Solution1()
    
    result = test.GetLeastNumbers_Solution([3,2,1,2,3,6,8,9,0,44,3,6,75,7,8,9,6,4,6,7,5,3,4,5,6,5],10)
    
    
    
    
    
    
    
    