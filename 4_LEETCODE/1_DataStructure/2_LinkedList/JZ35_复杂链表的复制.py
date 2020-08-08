class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        三步走：
        1. 复制节点；
        2. 复制指针；
        3. 奇偶拆分
        '''

        def copyNode(head):
            pNode = head

            while pNode:
                newNode = Node(pNode.val)
                newNode.next = pNode.next
                pNode.next = newNode
                pNode = pNode.next.next
            return head

        def copyRandom(head):
            pNode = head
            while pNode:
                cloneNode = pNode.next
                if pNode.random:
                    cloneNode.random = pNode.random.next
                pNode = pNode.next.next

            return head

        def splitList(head):
            headNodeOrigin = Node(-1)
            headNodeNew = Node(-1)
            pNodeOrigin = headNodeOrigin
            pNodeNew = headNodeNew

            pNode = head
            while pNode:
                pNodeOrigin.next = pNode
                pNodeNew.next = pNode.next
                pNodeOrigin = pNodeOrigin.next
                pNodeNew = pNodeNew.next
                pNode = pNode.next.next

            pNodeOrigin.next = None

            return headNodeOrigin.next, headNodeNew.next

        head = copyNode(head)
        head = copyRandom(head)
        _, headClone = splitList(head)

        return headClone