class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        

    # @return nothing
    def pop(self):
        tmpStack = []
        while self.stack:
            tmpStack.append(self.stack.pop())
        tmpStack.pop()
        while tmpStack:
            self.stack.append(tmpStack.pop())
        
            
            
        

    # @return an integer
    def peek(self):
        tmpStack = []
        while self.stack:
            tmpStack.append(self.stack.pop())
        ans = tmpStack[-1]
        while tmpStack:
            self.stack.append(tmpStack.pop())
        return ans
        

    # @return an boolean
    def empty(self):
        return len(self.stack)==0


if __name__ == '__main__':
    queue = Queue()
    queue.push(2)
    print queue.peek()
    queue.pop()
    print queue.empty()
