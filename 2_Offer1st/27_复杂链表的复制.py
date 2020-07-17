# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:55:11 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            pClone = None
            return pClone
        # write code here
        self.cloneNodes(pHead)
        self.connectRanNodes(pHead)
        return self.reconnectNodes(pHead)
    
    #复制形成2*n个节点数的交叉，有序单链。
    def cloneNodes(self,pHead):
        pNode = pHead
        while pNode != None:
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone    
            
            pNode = pClone.next
            
    
    #复制随机指针
    def connectRanNodes(self,pHead):
        pNode = pHead
        
        while pNode != None:
            pClone = pNode.next
            
            if pNode.random != None:
                pClone.random = pNode.random.next
            
            pNode = pClone.next
            
            
    #拆分奇偶链表
    def reconnectNodes(self,pHead):
        pNode = pHead
        
        if pNode != None:
            pCloneHead = pNode.next
            pCloneNode = pNode.next
            
            pNode.next = pCloneNode.next 
            pNode = pNode.next
            
        while pNode != None:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            
            pNode.next = pCloneNode.next
            pNode = pNode.next   
            
        return pCloneHead
            




if __name__ == '__main__':
    test = Solution()
    
    A = RandomListNode(1)
    B = RandomListNode(2)          
    C = RandomListNode(3)        
    D = RandomListNode(4)
    E = RandomListNode(5)

    A.next = B
    B.next = C
    C.next = D
    D.next = E

    A.random = C
    B.random = E
    D.random = B
    
    
    AClone = test.Clone(A)


