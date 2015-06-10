class Solution:
    def evalRPN(self,tokens):
        stack=[]
        for token in tokens:
           
            if token not in '+-/*':
                stack.append(int(token))
            else:
                
                if token is'+':
                    tmp=stack.pop()+stack.pop()
                    stack.append(tmp)
                elif token is '-':
                    tmp=stack[-2]-stack[-1]
                    stack=stack[:-2]
                    stack.append(tmp)
                elif token is '*':
                    tmp=stack.pop()*stack.pop()
                    stack.append(tmp)
                else:
                    if stack[-2]*stack[-1]<0:
                        tmp = -(abs(stack[-2])/abs(stack[-1]))
                    else:
                        tmp=stack[-2]/stack[-1]
                    stack=stack[:-2]
                    stack.append(tmp)
                
        top=stack.pop()
        if len(stack)==0:
            return top
        return -1
    def evalRPN1(self,tokens):
        stack=[]
        for token in tokens:
            if token not in '+-/*':
                stack.append(int(token))
            else:
                if token is '+':
                    stack.append(stack.pop() + stack.pop())
                elif token is '-':
                    stack.append(-stack.pop() + stack.pop())
                elif token is '*':
                    stack.append(stack.pop()*stack.pop())
                else:
                    tmp1 = stack.pop()
                    if tmp1 == 0:
                        return -1
                    stack.append(stack.pop()/tmp1)
        return stack[0] if len(stack) == 1 else -1

if __name__=='__main__':
    sol=Solution()
    tokens=["-3","9","*"]
    print sol.evalRPN(tokens)
    print sol.evalRPN1(tokens)
    
