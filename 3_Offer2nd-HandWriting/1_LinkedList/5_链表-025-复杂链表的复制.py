class RandomListNode:
    def __init__(self, value):
        self.label = value
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        pHead = self.cloneList(pHead)
        pHead = self.copyRandomP(pHead)
        pCloneHead = self.splitList(pHead)

        return pCloneHead

    def cloneList(self, pHead):
        pNode = pHead
        while pNode:
            cloneNode = RandomListNode(pNode.label)
            cloneNode.next = pNode.next
            pNode.next = cloneNode
            pNode = pNode.next.next

        return pHead

    def copyRandomP(self, pHead):
        pNode = pHead

        while pNode:
            cloneNode = pNode.next
            if pNode.random:
                cloneNode.random = pNode.random.next
            pNode = pNode.next.next
        return pHead

    def splitList(self, pHead):
        newHead = RandomListNode(-1)
        pNode = newHead
        newCloneHead = RandomListNode(-1)
        pCloneNode = newCloneHead

        while pHead:
            pNode.next = pHead
            pNode = pNode.next
            pCloneNode.next = pHead.next
            pCloneNode = pCloneNode.next
            pHead = pHead.next.next
        pNode.next = None

        return newCloneHead.next


if __name__ == '__main__':
    test = Solution()

    A = RandomListNode(1)
    B = RandomListNode(2)
    C = RandomListNode(3)
    D = RandomListNode(4)
    E = RandomListNode(5)

    A.next = B
    B.next = C
    C.next = D
    D.next = E

    A.random = C
    B.random = E
    D.random = B

    AClone = test.Clone(A)
    while AClone:
        print (AClone.label)
        AClone = AClone.next
