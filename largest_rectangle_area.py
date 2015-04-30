class Solution:
    def largestRectangleArea(self,height):
        stack=[]
        height.append(-1)
        length=len(height)
        sumArea=0
        index=0
        while index<length:
            if len(stack)==0 or height[stack[-1]]<=height[index]:
                stack.append(index)
                index+=1
            else:
                top=stack.pop()
                sumArea=max(sumArea,height[top]*(index if len(stack)==0 else index-stack[-1]-1))
        return sumArea


if __name__=='__main__':
    sol=Solution()
    height=[]
    print sol.largestRectangleArea(height)
