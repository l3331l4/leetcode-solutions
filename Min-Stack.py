class MinStack:

    def __init__(self):
        self.stack1 = []
        self.currMinStack = []
        
    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.currMinStack:
            self.currMinStack.append(val)
        elif val < self.currMinStack[-1]:
            self.currMinStack.append(val)    
        else:
            self.currMinStack.append(self.currMinStack[-1])     

    def pop(self) -> None:
        self.stack1.pop()
        self.currMinStack.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.currMinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()