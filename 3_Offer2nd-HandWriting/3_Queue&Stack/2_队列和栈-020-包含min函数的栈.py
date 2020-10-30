class MinStack:
    # 添加辅助栈，为了O(1_最短回文串.py)求最小值
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []   # 维护一个单调不增栈

    def push(self, x: int):
        if not self.minStack or self.minStack[-1] > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
        self.minStack.pop()
