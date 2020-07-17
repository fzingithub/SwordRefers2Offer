# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:44:21 2019

@author: zhe
"""
import heapq


#use two heapq to realize this problem.
class Solution:
    def __init__ (self):
        self.maxheap = []
        self.minheap = []
    def Insert(self, num):
        if (len(self.maxheap)+len(self.minheap))&1: #总数为奇数插入最大堆
            if len(self.minheap)> 0:  
                if num > self.minheap[0]:#大于最小堆里的元素
                    heapq.heappush(self.minheap, num)#新数据插入最小堆
                    heapq.heappush(self.maxheap, -self.minheap[0])#最小堆中的最小插入最大堆
                    heapq.heappop(self.minheap)
                else:
                    heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.maxheap, -num)
        else:                           #总数为偶数 插入最小堆
            if len(self.maxheap)> 0: #小于最大堆里的元素
                if num < -self.maxheap[0]:
                    heapq.heappush(self.maxheap, -num)#新数据插入最大堆
                    heapq.heappush(self.minheap, -self.maxheap[0])#最大堆中的最大元素插入最小堆
                    heapq.heappop(self.maxheap)
                else:
                    heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.minheap, num)
        #print (self.minheap)
    def GetMedian(self,n=None):
        if (len(self.maxheap)+len(self.minheap))&1:
            mid = self.minheap[0]
        else:
            mid = (self.minheap[0]-self.maxheap[0])/2.0
        return mid
