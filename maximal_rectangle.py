class Solution:
    def maximalRectangle(self,matrix):
        if len(matrix)==0:
            return 0
        h=[0 for i in range(len(matrix[0]))]
        maxArea=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    h[j]+=1
                else:
                    h[j]=0
            maxArea=max(maxArea,self.largestRectangleArea(h))
        return maxArea
        
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
    sol=Solution
    matrix=[['0','0','0','0'],['0','0','1','0'],['0','1','1','0'],['1','0','1','1']]
    print sol.maximalRectangle(matrix)
