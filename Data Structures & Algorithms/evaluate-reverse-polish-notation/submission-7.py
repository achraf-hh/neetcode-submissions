class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for t in tokens : 
            if t.isnumeric() or len(t) > 1:
                self.stack.append(int(t))
            else:
                if t == "+":
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.stack.append(val2 + val1)
                if t == "*":
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.stack.append(val2 * val1)
                if t == "-":
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.stack.append(val2 - val1)
                if t == "/":
                    val1 = self.stack.pop()
                    val2 = self.stack.pop()
                    self.stack.append(int(val2 / val1))
        return self.stack.pop()