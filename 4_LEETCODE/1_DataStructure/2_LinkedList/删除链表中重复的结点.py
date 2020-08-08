class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # 完全删除
    def deleteDuplication(self, pHead):
        pNewHead = ListNode(-1)

        pNodePre = pNewHead
        pNode = pHead

        while pNode:
            if pNode.next and pNode.val == pNode.next.val:
                pNodeSuc = pNode.next
                while pNodeSuc and pNodeSuc.val == pNode.val:
                    pNodeSuc = pNodeSuc.next
                pNodePre.next = pNodeSuc
                pNode = pNodeSuc
            else:
                pNodePre.next = pNode
                pNodePre = pNodePre.next
                pNode = pNode.next
        return pNewHead.next





    # 非完全删除
    def deleteDuplication2(self, pHead):
        pNode = pHead

        while pNode:
            if pNode.next and pNode.val == pNode.next.val:
                pdNode = pNode.next
                while pdNode and pdNode.val == pNode.val:
                    pdNode = pdNode.next
                pNode.next = pdNode
            pNode = pNode.next

        return pHead