class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        def getLength(pNode):
            res = 0
            while pNode:
                res += 1
                pNode = pNode.next
            return res

        lengthA = getLength(headA)
        lengthB = getLength(headB)
        difLength = abs(lengthB - lengthA)

        if lengthA > lengthB:
            pLong = headA
            pShort = headB
        else:
            pLong = headB
            pShort = headA

        while pLong and difLength > 0:
            pLong = pLong.next
            difLength -= 1

        while pLong and pShort:
            if pLong is pShort:
                return pLong
            pLong, pShort = pLong.next, pShort.next

        return None