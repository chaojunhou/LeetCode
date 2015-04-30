class Solution:
    def uniquePathWithObstacles(self,obstacleGrid):
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        dp=[[0 for x in range(cols)] for y in range(rows)]
       
        for i in range(cols):
            if obstacleGrid[0][i]==0:
                dp[0][i]=1
            else:
                dp[0][i]=0
                break
        print dp
        for j in range(rows):
            if obstacleGrid[j][0]==0:
                dp[j][0]=1
            else:
                dp[j][0]=0
                break
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[rows-1][cols-1]
    
    def uniquePathWithObstacles1(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for x in range(col+1)] for y in range(row+1)]
        dp[row][col-1] = 1
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1] if obstacleGrid[i][j] == 0 else 0
                print dp
        return dp[0][0]

if __name__=='__main__':
    sol=Solution()
    obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
    print sol.uniquePathWithObstacles1(obstacleGrid)
