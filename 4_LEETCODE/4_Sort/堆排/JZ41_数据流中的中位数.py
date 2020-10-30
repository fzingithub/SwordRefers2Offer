class MedianFinder:
    '''
    方法一：暴力解法
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []


    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()


    def findMedian(self) -> float:
        length = len(self.data)
        if not length:
            return None
        mid = length//2
        if length%2==0:
            return sum(self.data[mid-1:mid+1])/2
        else:
            return self.data[mid]

import heapq
class MedianFinder:
    '''
    方法二：优先队列
    两个优先队列
    A 小顶堆 存大一半元素
    B 大顶堆 存小一半元素
    两堆元素个数差值始终不超过1

    设元素总数为 N=m+n ，其中 m 和 n 分别为 A 和 B 中的元素个数。
    京东. 当 m = n（即 N 为 偶数）：需向 A 添加一个元素。实现方法：将新元素 num 插入至 B ，再将 B 堆顶元素插入至 A ；
    2. 当 m != n（即 N 为 奇数）：需向 B 添加一个元素。实现方法：将新元素 num 插入至 A ，再将 A 堆顶元素插入至 B ；

    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] # 大顶堆   进出取反即可   python heapq 只支持小顶堆
        self.B = [] # 小顶堆
        self.lengthA = 0
        self.lengthB = 0


    def addNum(self, num: int) -> None:
        if  self.lengthA!= self.lengthB:
            heapq.heappush(self.A, -num)
            heapq.heappush(self.B, -heapq.heappop(self.A))
            self.lengthB += 1
        else:
            heapq.heappush(self.B, num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
            self.lengthA += 1



    def findMedian(self) -> float:
        return -self.A[0] if self.lengthA!=self.lengthB else (-self.A[0]+self.B[0])/2
