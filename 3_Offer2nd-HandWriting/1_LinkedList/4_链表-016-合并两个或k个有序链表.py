class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # iteration
    def Merge(self, pHead1, pHead2):

        newHead = ListNode(-1)
        node = newHead

        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
            node = node.next

        node.next = pHead1 if pHead1 else pHead2

        return newHead.next

    # recursion
    def Merge2(self, pHead1, pHead2):
        if not pHead2:
            return pHead1
        if not pHead1:
            return pHead2

        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge2(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge2(pHead1, pHead2.next)
            return pHead2


