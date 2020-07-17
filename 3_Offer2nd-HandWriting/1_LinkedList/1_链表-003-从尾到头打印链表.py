class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def printListFromTail2Head(self, listNode):
        stack = []
        res = []

        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next

        while stack:
            res.append(stack.pop())

        return res

