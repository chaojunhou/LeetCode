class Solution:
    def maxProfit(self,prices):
        profit=0
        for i in range(1,len(prices)):
            
            if prices[i]>prices[i-1]:
                profit=profit+prices[i]-prices[i-1]
                print profit
        return profit

    #search a up sorted list 

if __name__=='__main__':
    hou=Solution()
    prices=[2,1]
    print hou.maxProfit(prices)
