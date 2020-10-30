class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def merge_list(self, pHead):
        '''
        快慢指针， 二路归并
        '''
        def merge(p1, p2):
            if not p1:
                return p2
            if not p2:
                return p1
            if p1.val < p2.val:
                p1.next = merge(p1.next, p2)
                head = p1
            else:
                p2.next = merge(p1, p2.next)
                head = p2
            return head


        if  not pHead or not pHead.next:
            return pHead

        pslow = pHead
        pfast = pHead.next

        while pfast and pfast.next:
            pslow = pslow.next
            pfast = pfast.next.next

        pmid = pslow.next
        pslow.next = None

        left = self.merge_list(pHead)
        right = self.merge_list(pmid)

        return merge(left, right)




    def quickSort_List(self, pHead):
        '''
        快速排序
        '''
        if not pHead or not pHead.next:
            return pHead

        pLHead = ListNode(-1)
        pEHead = ListNode(-1)
        pGHead = ListNode(-1)
        pLNode = pLHead
        pENode = pEHead
        pGNode = pGHead

        k = pHead.val
        while pHead:
            if pHead.val<k:
                pLNode.next = pHead
                pLNode = pLNode.next
            elif pHead.val == k:
                pENode.next = pHead
                pENode = pENode.next
            else:
                pGNode.next = pHead
                pGNode = pGNode.next
            pHead = pHead.next

        pLNode.next, pENode.next, pGNode.next = None, None, None

        pleft = self.quickSort_List(pLHead.next)
        pRight = self.quickSort_List(pGHead.next)
        pEHead = pEHead.next

        pNewHead = ListNode(None)
        cur = pNewHead

        for p in [pleft, pEHead, pRight]:
            while p is not None:
                cur.next = p
                p = p.next
                cur = cur.next
                cur.next = None
        return pNewHead.next

if __name__ == '__main__':
    test = Solution()
    import random

    pHead = ListNode(-1)
    pNode = pHead

    for i in range(20):
        pNode.next = ListNode(random.randint(0,30))
        pNode = pNode.next

    pNode = pHead.next
    res = []
    while pNode:
        res.append(pNode.val)
        pNode = pNode.next

    print(res)
    pHead = test.quickSort_List(pHead.next)

    res = []
    while pHead:
        res.append(pHead.val)
        pHead = pHead.next

    print(res)