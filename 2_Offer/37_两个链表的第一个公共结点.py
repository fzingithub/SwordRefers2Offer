# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:47:15 2019

@author: zhe

E-mail: 1194585271@qq.com
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
#解法一，O(m+n) O(2*min(List))
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        stack1 = []
        stack2 = []
        
        while pHead1:
            stack1.append(pHead1)
            pHead1=pHead1.next
            
        while pHead2:
            stack2.append(pHead2)
            pHead2=pHead2.next
        
        preNode = None
        while stack1 and stack2 and stack1[-1]==stack2[-1]:
            preNode = stack1.pop()
            stack2.pop()
            
        return preNode
        
                    

#解法二，O(m+n) O(1)
class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        nlength1 = self.getListLength(pHead1)
        nlength2 = self.getListLength(pHead2)
        
        nlengthdiff = nlength1 - nlength2
        
        pListHeadLong = pHead1
        pListHeadShort = pHead2
        
        if nlength2 > nlength1:
            nlengthdiff = nlength2 - nlength1
            pListHeadLong = pHead2
            pListHeadShort = pHead1
        
        #长链表先走nlengthdiff步
        for i in range(nlengthdiff):
            pListHeadLong = pListHeadLong.next
            
        #同步加入栈中
        while pListHeadLong and pListHeadShort and pListHeadLong is not pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next
            
            
        pFirstCommomNode = pListHeadLong
        return pFirstCommomNode
    
    def getListLength(self,pHead):
        i = 0
        pNode = pHead
        while pNode:
            i =  i + 1
            pNode = pNode.next
        return i
    
if __name__=='__main__':
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    F = ListNode(6)
    A.next = D
    D.next = E
    E.next = F
    
    B.next = C
    C.next = D
    
    test = Solution1()
    res = test.FindFirstCommonNode(A,B)
    print (res.val)
    
    
            
