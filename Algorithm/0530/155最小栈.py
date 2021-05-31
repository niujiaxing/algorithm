class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(self.stack))



    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]
