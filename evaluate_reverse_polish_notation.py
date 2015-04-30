class Solution:
    def evalRPN(self,tokens):
        stack=[]
        for token in tokens:
            print stack
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
                        tmp=-(abs(stack[-2])/abs(stack[-1]))
                        print tmp
                    else:
                        tmp=stack[-2]/stack[-1]
                    stack=stack[:-2]
                    stack.append(tmp)
                print stack
        top=stack.pop()
        if len(stack)==0:
            return top
        return -1


if __name__=='__main__':
    sol=Solution()
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print sol.evalRPN(tokens)
    
