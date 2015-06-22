class Solution:
    def minimumTotal(self,triangle):
        length=len(triangle)
        dp=[0 for x in range(length)]
        for row in triangle:
            for i in range(len(row)-1,-1,-1):
                if i==0:
                    dp[i]=dp[i]+row[i]
                elif i ==len(row)-1:
                    dp[i]=dp[i-1]+row[i]
                else:
                    dp[i]=min(dp[i],dp[i-1])+row[i]
        return min(dp)
    def minimumTotal_1(self,triangle):
        length=len(triangle)
        dp=[0 for x in range(length)]
        for i in range(length-1,-1,-1):
            for j in range(len(triangle[i])):
                if i==length-1:
                    dp[j]=triangle[i][j]
                    continue
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        return dp[0]
                    
                

if __name__=='__main__':
    sol=Solution()
    triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
    print sol.minimumTotal(triangle)
    print sol.minimumTotal_1(triangle)
