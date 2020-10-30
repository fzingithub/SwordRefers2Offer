class MaxQueue:

    def __init__(self):
        self.queue = []
        self.IO2Queue = []  # 维护一张单调非减的双端队列 [5,3,3,1_最短回文串.py]

    def max_value(self):
        if not self.queue:
            return -1
        else:
            return self.IO2Queue[0]

    def push_back(self, value):
        while self.IO2Queue and self.IO2Queue[-1] < value:
            self.IO2Queue.pop()
        self.IO2Queue.append(value)

        self.queue.append(value)

    def pop_front(self):
        if not self.queue:
            return -1

        value = self.queue.pop(0)
        if value == self.IO2Queue[0]:
            self.IO2Queue.pop(0)

        return value

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()