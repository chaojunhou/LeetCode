class Solution:
    def maxProfit (self,k,prices):
        length = len (prices)
        if length < 2 :
            return 0
        if k> length/2:
            maxprofit = 0
            for i in range(1,length):
                if prices[i] > prices[i-1]:
                    maxprofit += prices[i] - prices[i-1]
            return maxprofit
        dp = [[0 for i in range(length)] for j in range(k+1)]
        for i in range(1, k+1):
            tmp = -prices[0]
            for j in range(1,length):
                dp [i][j] = max(dp[i][j-1],prices[j]+tmp)
                tmp = max (tmp, dp[i-1][j-1] - prices[j])
        return dp [k][length-1]
            


if __name__ == '__main__':
    sol = Solution()
    prices = [1,3,4,9,2,0,10,6,4]
    k=10
    print sol.maxProfit (k,prices)
    
