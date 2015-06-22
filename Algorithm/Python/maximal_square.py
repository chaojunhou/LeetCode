class Solution:
    def maximalSquare1(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        A = [[0 for i in range(n+1)] for j in range(m)]
        area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    A [i][j] += 1 if i==0 else A[i-1][j]+1
            area = max(area, self.largestSquareArea(A[i]))
            print area, self.largestSquareArea(A[i])
            print A
        return area
    def largestSquareArea(self,height):
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
    def maximalSquare (self,matrix):
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        maxSize = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])

            maxSize = max(dp[i][0], maxSize)
        for j in range(1,n):
            dp[0][j] = int(matrix[0][j])
            maxSize = max(dp[0][j], maxSize)
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    if dp[i][j] > maxSize:
                        maxSize = dp[i][j]
        return maxSize*maxSize
    def maximalSquare2 (self,matrix):
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        maxSize = 0
        for j in range(n):
            if matrix[0][j] == '1':
                maxSize = 1 
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1]))+1
                    if matrix[i][j] > maxSize:
                        maxSize = matrix[i][j]
        return maxSize*maxSize    
        
if __name__  == '__main__':
    sol = Solution()
    matrix = [[1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0],
              ]
    #matrix = [1]
    #matrix = [0,1]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = str(matrix[i][j])
    print sol.maximalSquare1(matrix)
