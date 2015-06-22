class Solution:
    def maxProfit(self,prices):
        if not prices:
            return 0
        down=prices[0]
        length=len(prices)
        maxProfit=0
        for index in range(1,length):
            
            profit=prices[index]-down
            if down>prices[index]:
                down=prices[index]
            if maxProfit<profit:
                maxProfit=profit
            print maxProfit
                
        return maxProfit

if __name__=='__main__':
    sol=Solution()
    import random
    prices=[random.randint(0,100) for x in range(10)]
    print prices
    print sol.maxProfit(prices)
