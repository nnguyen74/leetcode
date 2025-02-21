from collections import deque
class MinStack:

    def __init__(self):
        self.minStack = deque()

    def push(self, val: int) -> None:
        if not self.minStack:
            self.minStack.append((val, val))
        else:
            _, currentMin = self.minStack[-1]
            self.minStack.append((val, min(val, currentMin)))

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1][0]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()