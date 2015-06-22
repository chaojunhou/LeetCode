class Solution:
    def minPathSum(self,grid):
        rows=len(grid)
        cols=len(grid[0])
     
        dp=[[0 for x in range(cols)] for y in range(rows)]
        print dp
        
        for i in range(0,rows):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(0,cols):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[rows-1][cols-1]


if __name__=='__main__':
    sol=Solution()
    import random
    grid=[[random.randint(1,100) for x in range(9)] for y in range(11)]
    grid=[[0]]
    print sol.minPathSum(grid)
