class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
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
            if len(stack)==0 or height[stack[-1]] <= height[index]:
                stack.append(index)
                index+=1
            else:
                top=stack.pop()
                sumArea=max(sumArea,height[top]*(index if len(stack)==0 else index-stack[-1]-1))
        return sumArea
    def maximalRectangle1(self, matrix):
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])

        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        height = [0 for i in range(n)]
        maxArea = 0
        for i in range(m):
            curLeft = 0
            curRight = n
            print left, right, height
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min (right[j], curRight)
                else:
                    right[j] = n
                    curRight = j
          
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],curLeft)
                    height[j] += 1
                else:
                    height[j] = 0
                    left[j] = 0
                    curLeft = j+1
                
                maxArea = max(maxArea, (right[j]- left[j])*height[j])
            print left, right, height, maxArea
        return maxArea

if __name__=='__main__':
    sol=Solution()
    matrix = [['0','0','0','1','0','0','0'],
              ['0','0','1','1','1','0','0'],
              ['0','1','1','1','1','1','0'],]       
    #matrix = ['1']
    #print sol.maximalRectangle(matrix)
    print sol.maximalRectangle1(matrix)
    
