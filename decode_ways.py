class Solution:
    def numDecodeings(self,s):
        n = len(s) +1
        if n == 1 or s[0]=='0':
            return 0
        dp=[0 for i in range(n)]
        dp[0]=1
        dp[1]=1
        for i in range(2,n):
            tmp = s[i-2:i]
            if '10'<=tmp<= '26' :
                if tmp == '10' or tmp == '20': 
                    dp[i]=dp[i-2]
                else:
                    dp[i]=dp[i-1]+dp[i-2]
            elif s[i-1]!='0':  # 41, only can reach i from i-1
                dp[i]=dp[i-1]
            else:
                return 0
        return dp[n-1]
if __name__=='__main__':
    sol=Solution()
    s='123'
    print sol.numDecodeings(s)
