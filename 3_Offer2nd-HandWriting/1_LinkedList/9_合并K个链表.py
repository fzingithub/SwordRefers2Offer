class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        '''
        暴力解法: NlogN 空间 N
        '''
        nums = []
        for node in lists:
            while node:
                nums.append(node.val)
                node = node.next

        nums.sort()

        pre = ListNode(-1)

        node = pre
        for i in nums:
            node.next = ListNode(i)
            node = node.next

        return pre.next


    def mergeKLists(self, lists):
        '''
        优先队列： NlogK  K
        '''
        import heapq

        heap, cur = [], []  # 初始化优先队列，建立链表索引

        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index))
            cur.append(node)

        pre = ListNode(-1)
        node = pre

        while heap:
            val, index = heapq.heappop(heap)
            node.next = ListNode(val)
            node = node.next

            cur[index] = cur[index].next
            if cur[index]:
                heapq.heappush(heap, (cur[index].val, index))

        return pre.next

    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return None

        interval = 1
        while interval < length:
            for i in range(0, length - interval, interval * 2):
                lists[i] = self.Merge(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)

        return pMergeHead
