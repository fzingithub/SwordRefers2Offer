class CQueue:

    def __init__(self):
        self.Stack1 = []  # 入队栈
        self.Stack2 = []  # 出队栈

    def appendTail(self, value):
        self.Stack1.append(value)

    def deleteHead(self):
        if self.Stack2:
            return self.Stack2.pop()
        elif self.Stack1:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())

            return self.Stack2.pop()
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()