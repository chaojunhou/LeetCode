import collections
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = collections.deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        n = len(self.queue)
        while n != 0 :
            self.queue.appendleft(self.queue.pop())
            n -= 1
        self.queue.appendleft(x)
    # @return nothing
    def pop(self):
        print self.queue
        return self.queue.popleft()

    # @return an integer
    def top(self):
        return self.queue[0]       
    # @return an boolean
    def empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':

    Stack = Stack()
    Stack.push(1)

    print Stack.pop()
    Stack.push(5)
    print Stack.top()
    
