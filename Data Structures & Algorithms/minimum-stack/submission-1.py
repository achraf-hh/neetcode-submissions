class MinStack:

    def __init__(self):
        self.Minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        
        if self.stack == []:
            self.stack.append(val)
            self.Minstack.append(val)
        else:
            currMin = self.Minstack[-1]
            if currMin > val:
                currMin = val
                self.stack.append(val)
                self.Minstack.append(val)
            else:
                self.stack.append(val)
                self.Minstack.append(currMin)



    def pop(self) -> None:
        self.Minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Minstack[-1]
        
