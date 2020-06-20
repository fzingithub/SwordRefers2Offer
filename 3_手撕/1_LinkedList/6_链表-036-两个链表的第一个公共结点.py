class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None

        length1 = self.getListLength(pHead1)
        length2 = self.getListLength(pHead2)

        if length1>length2:
            difLength = length1 - length2
            pListShortHead = pHead2
            pListLongHead = pHead1
        else:
            difLength = length2 - length1
            pListShortHead = pHead1
            pListLongHead = pHead2

        while difLength>0:
            pListLongHead = pListLongHead.next
            difLength -= 1

        while pListLongHead and pListShortHead and pListShortHead is not pListLongHead:
            pListLongHead = pListLongHead.next
            pListShortHead = pListShortHead.next

        return pListShortHead


    def getListLength(self, pHead):
        length = 0
        while pHead:
            pHead = pHead.next
            length += 1

        return length


