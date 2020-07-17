class Solution:
    def validateStackSequences(self, pushed, popped):

        if not pushed:
            return True

        stack = []  # 设立辅助栈，观测pop序列
        while popped:
            if not stack or popped[0] != stack[-1]:
                if not pushed: # 当此时栈顶元素与观测序列当前值不相等且pushed列表为空时返回 False
                    return False
                else:
                    stack.append(pushed.pop(0)) # 否则入栈
            else:   # 观测序列当前值与栈顶元素相等
                stack.pop()
                popped.pop(0)

        return True




