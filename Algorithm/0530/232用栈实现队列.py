class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.outstack) == 0 and len(self.instack) == 0

## 时间复杂度 pop O(N)或O(1)    push  O(1)   peek   O(N)   O(1)    empty O(1)
##空间复杂度 O（N）
