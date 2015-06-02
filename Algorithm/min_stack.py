"""class MinStack:
    ordinary=[]
    minimium=[]
    def __init__(self):
        self.ordinary = []
        self.minimium = []
    def push(self,x):
        #ordinary.append(x)
        self.ordinary.append(x)
        if len(self.minimium) == 0:
            self.minimium.append(x)       
        else:
            self.minimium.append(min(x,self.minimium[-1]))
        
        return self.minimium[-1]
    def pop(self):
        if self.minimium is not []:
            self.minimium.pop()
            self.ordinary.pop()

    def top(self):
        if self.ordinary is []:
            return -1
        return self.ordinary[-1]
    def getMin(self):
        if self.minimium is []:
            return -1
        return self.minimium[-1]
    """
class MinStack:
    # @param x, an integer
    # @return an integer
    stack, minStack = [], []
    global stack, minStack
    def push(self, x):
        stack.append(x)
        if not minStack or minStack[-1] >= x:
            minStack.append(x)
        return minStack[-1]
    # @return nothing
    def pop(self):
        if not stack:
            return
        if stack.pop() == minStack[-1]:
            minStack.pop()
    # @return an integer
    def top(self):
        return stack[-1] if  stack else -1

    # @return an integer
    def getMin(self):
        return minStack[-1] if minStack else -1
if __name__=='__main__':
    sol=MinStack()
    lst=[2,3,4,7,4,8,3,6,4,1,6]
    for element in lst:
        sol.push(element)
    print sol.top()
    sol.pop()
    sol.pop()
    print sol.getMin()
