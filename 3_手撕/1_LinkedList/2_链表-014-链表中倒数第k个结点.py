class listNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if k<0 or not head:
            return None

        FNode = head
        TNode = head

        while k:
            if FNode:
                FNode = FNode.next
                k -= 1
            else:
                return None

        while FNode:
            FNode = FNode.next
            TNode = TNode.next

        return TNode



