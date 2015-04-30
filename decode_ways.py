class Solution:
    def numDecodeings(self,s):
        if len(s)==0 or s[0]=='0':
            return 0
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        dp[1]=1
        for i in range(2,len(s)+1):
            number=int(s[i-2:i])
            if 10<=number<=26 :
                if number==10 or number==20:
                    dp[i]=dp[i-2]
                else:
                    dp[i]=dp[i-1]+dp[i-2]
            elif s[i-1]!='0':
                dp[i]=dp[i-1]
            else:
                return 0
        return dp[len(s)]
if __name__=='__main__':
    sol=Solution()
    s='10'
    print sol.numDecodeings(s)
