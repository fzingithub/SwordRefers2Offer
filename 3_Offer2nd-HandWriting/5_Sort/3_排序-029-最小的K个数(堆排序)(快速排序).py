class Solution:
    '''
    方法一：排序-快排 O(nlogn) 空间O(1)
    方法二：快排 partation O(n) 空间O(1)
    方法三：堆排 O(nlogk) 空间O(k)
    '''

    # 快排
    # 时间复杂度分析 假设quickSearch的时间复杂度为T(n),因为每次quickSearch里面会使得数据规模减半，则有 T(n) = T(n/2) + O(n) = T(n/4)+O(n)+O(n/2) = T(n/8)+O(n)+(n/2)+O(n/)4 = .... = O(n)+O(n/2)+O(n/4) +....+O(n/(2^(n-1))); 根据等比数列求和得出T(n) = 2O(n) = O(n)
    def getLeastNumbers1(self, arr, k):
        if not arr or not k:
            return []

        length = len(arr)
        return self.getLeastNumbersMain(arr, k, 0, length - 1)

    def getLeastNumbersMain(self, arr, k, left, right):
        if left <= right:
            index = self.partition(arr, left, right)
            if index == k - 1:
                return arr[:k]
            if index < k - 1:
                return self.getLeastNumbersMain(arr, k, index + 1, right)
            else:
                return self.getLeastNumbersMain(arr, k, left, index - 1)

    def partition(self, arr, left, right):
        '''
        左右指针
        :return: index of target value， int
        '''
        tarVal = arr[left]

        low = left
        high = right

        while low < high:
            while low < high and arr[high] > tarVal:
                high -= 1
            while low < high and arr[low] <= tarVal:
                low += 1

            if low < high:
                arr[high], arr[low] = arr[low], arr[high]

        arr[high], arr[left] = arr[left], arr[high]

        return high


    # 堆排 O(nlogk)
    def getLeastNumbers(self, arr, k):
        if not arr or not k:
            return []
        import heapq
        hq = list(map(lambda x:-x, arr[:k]))
        heapq.heapify(hq)

        for i in arr[k:]:
            if -i>hq[0]:
                hq[0] = -i
                heapq.heapify(hq)
        return list(map(lambda x:-x, hq))

if __name__== '__main__':
    test = Solution()
    res = test.getLeastNumbers([3,2,1], 2)
    print(res)
