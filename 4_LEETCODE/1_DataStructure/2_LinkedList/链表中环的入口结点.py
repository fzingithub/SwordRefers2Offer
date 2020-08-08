class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None

        pNodeFast = pHead.next.next
        pNodeSlow = pHead.next

        while pNodeFast is not pNodeSlow and pNodeFast and pNodeFast.next:
            pNodeFast = pNodeFast.next.next
            pNodeSlow = pNodeSlow.next

        if pNodeSlow is pNodeFast:
            pNodeSlow = pHead
        else:
            return None

        while pNodeSlow is not pNodeFast:
            pNodeSlow = pNodeSlow.next
            pNodeFast = pNodeFast.next

        return pNodeFast

