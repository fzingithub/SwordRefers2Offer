
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        newNode = ListNode(-1)
        newNode.next = head

        pFra = head
        pSon = newNode

        while pFra:
            if pFra.val == val:
                pSon.next = pFra.next
                break
            pFra, pSon = pFra.next, pSon.next

        return newNode.next
