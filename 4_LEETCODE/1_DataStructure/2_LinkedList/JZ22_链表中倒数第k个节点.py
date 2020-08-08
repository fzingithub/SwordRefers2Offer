class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        pFro, pBeh = head, head

        while pFro and k > 0:
            pFro = pFro.next
            k -= 1

        if k > 0:
            return None

        while pFro:
            pBeh, pFro = pBeh.next, pFro.next

        return pBeh
