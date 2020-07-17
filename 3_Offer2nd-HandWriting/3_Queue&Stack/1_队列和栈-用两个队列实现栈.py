class Stack:
    def __init__(self):
        self.Queue1 = []      # 入栈队， 出栈队
        self.Queue2 = []      # 反转队

    def push(self, value):
        self.Queue1.append(value)

    def pop(self): # return value
        while self.Queue1 and len(self.Queue1)!=1:
            self.Queue2.append(self.Queue1.pop(0))

        if self.Queue1:
            self.Queue1, self.Queue2 = self.Queue2, self.Queue1
            return self.Queue2.pop(0)
        else:
            return -1

if __name__ == '__main__':
    test = Stack()

    for i in range(5):
        test.push(i)

    for _ in range(3):
        print(test.pop())

    for i in range(5,10):
        test.push(i)

    for _ in range(10):
        print(test.pop())


