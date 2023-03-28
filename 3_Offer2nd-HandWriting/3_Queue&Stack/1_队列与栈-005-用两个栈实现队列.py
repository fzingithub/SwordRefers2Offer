class CQueue:

    def __init__(self):
        self.StackIn = []  # 入队栈
        self.StackOut = []  # 出队栈

    def appendTail(self, value):
        self.StackIn.append(value)

    def deleteHead(self):
        if self.StackOut:
            return self.StackOut.pop()
        elif self.StackIn:
            while self.StackIn:
                self.StackOut.append(self.StackIn.pop())

            return self.StackOut.pop()
        else:
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()