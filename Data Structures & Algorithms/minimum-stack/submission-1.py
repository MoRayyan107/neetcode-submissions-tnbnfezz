class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            minVal = min(val, self.min_stack[-1])
            self.min_stack.append(minVal)
        

    def pop(self) -> None:
        if len(self.stack) < 0 and len(self.min_stack) < 0:
            return None

        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
