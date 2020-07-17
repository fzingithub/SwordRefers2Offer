# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:53:35 2018

@author: zhe

E-mail: 1194585271@qq.com
"""
#两个栈实现一个队列
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        # write code here
        self.stack1.append(node)
                
    def pop(self):
        # return xx
        if len(self.stack2)!=0:
            return self.stack2.pop()
        else :
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

#两个队列实现一个栈
class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self,node):
        self.queue1.append(node)
        
    def pop(self):
        if len(self.queue1)==0:
            return None
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1,self.queue2 = self.queue2,self.queue1
        return self.queue2.pop()
            
        
if __name__=='__main__':
    times=5
    testList=list(range(times))
    testStock=Stack()
    for i in range(times):
        testStock.push(testList[i])
    print(testList)
    for i in range(times):
        print(testStock.pop(),' ',end='')   

        