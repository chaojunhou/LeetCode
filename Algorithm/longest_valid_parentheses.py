class Solution:
    def longestValidParentheses(self,s):
        length=len(s)
        stack=[]
        start=-1
        longest=0
        for i in range(length):
            if s[i]=='(':
                stack.append(i)
            else:
                
                if len(stack)==0 :
                    start=i
                else:
                    stack.pop()
                    if len(stack)==0:
                        longest=max(longest,i-start)
                    else:
                        longest=max(longest,i-stack[-1])
        return longest
    def longestValidParentheses_1   (self,s):
        stack=[(-1,')')]
        
        maxLen=0
        for i in range(len(s)):
            if s[i]==')' and stack[-1][1]=='(':
                stack.pop()
                maxLen=max(maxLen,i-stack[-1][0])
            else:
                stack.append((i,s[i]))

        return maxLen
               
        
            
            
        


if __name__=='__main__':
    sol=Solution()
    s='()(()'
    print sol.longestValidParentheses(s)
    print sol.longestValidParentheses_1(s)
