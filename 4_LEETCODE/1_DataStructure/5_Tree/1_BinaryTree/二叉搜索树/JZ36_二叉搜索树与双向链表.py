class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.pHead = None
        self.pTail = None

        def midTravesal(root):
            if not root:
                return

            midTravesal(root.left)

            if not self.pHead:
                self.pHead = root
                self.pTail = root
            else:
                self.pTail.right = root
                root.left = self.pTail
                self.pTail = root

            midTravesal(root.right)

        midTravesal(root)
        self.pHead.left, self.pTail.right = self.pTail, self.pHead

        return self.pHead
