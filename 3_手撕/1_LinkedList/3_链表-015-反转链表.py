class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # iteration
    def ReverseList(self, pHead):
        if not pHead:
            return None

        FNode = None
        TNode = pHead.next

        while TNode:
            pHead.next = FNode
            FNode = pHead
            pHead = TNode
            TNode = TNode.next
        pHead.next = FNode

        return pHead

    # recursion
    def ReverseList2(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        newHead = self.ReverseList2(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return newHead



if __name__ == '__main__':
    pNode = None

    for i in range(5):
        node = ListNode(i)
        node.next = pNode
        pNode = node

    test = Solution()

    pNode= test.ReverseList2(node)

    while pNode:
        print(pNode.val)
        pNode = pNode.next

