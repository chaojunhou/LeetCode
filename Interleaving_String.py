class Solution:
    def isInterleave(self,s1,s2,s3):
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)
        if len1+len2!=len3:
            return False
        dp=[[False for j in range(len2+1)] for i in range(len1+1)]
        dp[0][0]=True
        for i in range(1,len1+1):
            if s1[i-1]==s3[i-1]:
                dp[i][0]=dp[i-1][0]

        for j in range(1,len2+1):
            if s2[i-1]==s3[i-1]:
                dp[0][j]=dp[0][j-1]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if s1[i-1]==s3[i+j-1]:
                    dp[i][j]=dp[i-1][j]
                if s2[j-1]==s3[i+j-1]:
                    dp[i][j]=dp[i][j-1]
        return dp[len1][len2]
if __name__=='__main__':
    sol=Solution()
    s1='aabcc'
    s2='dbbca'
    s3='aadbbcbcac'
    print sol.isInterleave(s1,s2,s3)
