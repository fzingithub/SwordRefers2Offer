# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:46:51 2018

@author: zhe

E-mail: 1194585271@qq.com
    """

#不带头节点单链表
class listNode:
    def __init__(self,val=None,next=None):
        self.next = next
        self.val = val
        
class Solution:
    #返回链表根节点
    def deleteNodeO1(self,rNode,delNode):
        #参数节点为空
        if rNode.next == None or delNode == None:
            return None
        #被删节点不是最后一个节点
        if delNode.next != None:
            delNode.val = delNode.next.val
            delNode.next = delNode.next.next
            return rNode
        #被删节点是链表中的唯一节点
        elif delNode.next == None and delNode == rNode:
            rNode = None
            del delNode
            return rNode
        #被删节点是最后一个节点，链表中有多个节点
        else:
            tNode = rNode
            while tNode.next != delNode:
                tNode = tNode.next
            tNode.next = None
            del delNode
            return rNode
            
        
if __name__ == '__main__':
    listNode = listNode('A',(listNode('B',listNode('C',listNode('D')))))
#    listNode = listNode('A')
    rNode = listNode
#    while True:
#        print(listNode.val)
#        if listNode.next != None:
#            listNode = listNode.next
#        else:
#            break
        
    while True:
        if listNode.val == 'C':
            break
        listNode = listNode.next
        
        
    testDel = Solution()
    ADelRNode = testDel.deleteNodeO1(rNode,listNode)
    
    while True:
        if ADelRNode == None:
            break
        print(ADelRNode.val)
        if ADelRNode.next != None:
            ADelRNode = ADelRNode.next
        else:
            break