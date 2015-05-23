class Solution:
    def rob(self,num):
        length = len(num)
        if length == 0:
            return 0
        dp = [0 for x in range(length)]
        dp[0]=num[0]
        dp[1]=max(num[0],num[1])
        for i in range(2,length):
            dp[i] = max(dp[i-2]+num[i],dp[i-1])
        return  dp[length-1]
    def rob1(self,num):
        length = len(num)
        dp = [[0 for y in range(2)] for x in range(length)]
        dp[0][1] = num[0]
        dp[0][0] = 0
        for i in range (1,length):
            dp[i][1]=max(dp[i-1][0],dp[i-1][0]+num[i])
            dp[i][0]=max(dp[i-1][1],dp[i-1][0])
        return  dp[length-1][1] if dp[length-1][1] > dp[length-1][0] else dp[length-1][0]
            
        


if __name__ == '__main__':
    sol = Solution()
    num=[2,1,1,2]
    print sol.rob(num)
        
