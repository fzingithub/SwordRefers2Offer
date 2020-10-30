class Solution:
    def matSort(self, data):
        '''
        :param data:  二维有序数组
        :return:  一维全有序数组

        方法一： 暴力 O(knlogkn) 空间 O(n)
        '''

        return sorted(sum(data, []))

    def matSort1(self, data):
        '''
        :param data:  二维有序数组
        :return:  一维全有序数组

        方法二： 多路归并 O(nlogk)
        '''
        def merge(nums1, nums2):
            data = []
            while nums1 and nums2:
                if nums1[0]<nums2[0]:
                    data.append(nums1.pop(0))
                else:
                    data.append(nums2.pop(0))

            data.extend(nums1) if nums1 else data.extend(nums2)

            return data

        m = len(data)

        interval = 1
        while interval<m:
            for i in range(0, m-interval, interval*2):
                data[i] = merge(data[i], data[i+interval])
            interval *= 2

        return data[0]

    def matSort3(self, data):
        '''
        :param data:  二维有序数组
        :return:  一维全有序数组

        方法二： 优先队列 O(nlogk)
        '''
        import heapq
        m = len(data)
        res = []

        hq = [(pHead.pop(0), i) for i, pHead in enumerate(data)]
        heapq.heapify(hq)
        while hq:
            value, index = heapq.heappop(hq)
            res.append(value)
            if data[index]:
                heapq.heappush(hq, (data[index].pop(0), index))
            heapq.heapify(hq)
        return res

if __name__ == '__main__':
    test = Solution()

    data = [
        [1,5,10,15,20,25],
        [2,6,11,16,21,26],
        [3,7,12,17,22,27],
        [4,8,13,18,23,28]
    ]

    res = test.matSort3(data)

    print(res)

