class Solution:
    def calculateMinimumHP_1(self,dungeon):
        m=len(dungeon)
        n=len(dungeon[0])
        hp=0
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        dp[m-1][n]=1
        dp[m][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=max(1,mindp[i+1][j]-dungeon[i][j],dp[i][j+1]-dungeon[i][j])
        return dp[0][0]
    def calculateMinimumHP(self,dungeon):
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[2**20 for i in range(n+1)] for j in range(m+1)]
        dp[m-1][n]=1
        dp[m][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                need=min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                dp[i][j]=1 if need<=0 else need
        return dp[0][0]
        
if __name__=='__main__':
    sol=Solution()
    dungeon=[[5,23,-48,-21,-72,-62,-19,-55,-3,-93,-84,14,-34,46,-82,-46,39,26,47,-71,-46,-3,-59,-93,-13,-72,19,-43,-51,-2,-6,-53,12,-40,15,-94,37,-3,-32,-97]]
    print sol.calculateMinimumHP_1(dungeon)
