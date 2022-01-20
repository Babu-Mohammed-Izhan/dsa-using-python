# Design a class to implement a stack using only a single queue. 
# Your class, QueueStack, should support the following stack methods:
#  push() (adding an item), pop() (removing an item), peek() (returning the top value without removing it), 
# and empty() (whether or not the stack is empty).



class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x: int) -> None:
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self) -> int:
        return self._queue.popleft()
       
    def top(self) -> int:
        return self._queue[0]
        

    def empty(self) -> bool:
        if len(self._queue) == 0 :
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()