class Solution:
    def minDistance(self,word1,word2):
        n=len(word1)
        m=len(word2)  
        dp=[[0 for x in range(m+1)] for y in range(n+1)]
        for j in range(m+1):
            dp[0][j]=j
        for i in range(n+1):
            dp[i][0]=i
        for i in range(0,n):
            for j in range(0,m):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=min(dp[i][j+1]+1,dp[i+1][j]+1,dp[i][j])
                else:
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
        return dp[n][m]
    def minDistance1(self,word1,word2):
        n=len(word1)
        m=len(word2) 
        dp=[[2**10 for x in range(m+1)] for y in range(n+1)]
        for j in range(m):
            dp[n][j]= m-j
        for i in range(n):
            dp[i][m] = n-i
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=min(dp[i][j+1]+1,dp[i+1][j]+1,dp[i+1][j+1])
                else:
                    dp[i][j]=min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])+1
        return dp[0][0]
if __name__=='__main__':
    sol=Solution()
    word1='pneumonoultramicroscopicsilicovolcanoconiosis'
    word2='ultramicroscopically'
    print sol.minDistance(word1,word2)
    print sol.minDistance1(word1,word2)
