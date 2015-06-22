class Solution:
    def maxProfit(self,prices):
        length=len(prices)
        left=[0 for x in range(length)]
        right=[0 for x in range(length)]
        minLeft=prices[0]
        for i in range(1,length):
            if prices[i]<minLeft:
                minLeft=prices[i]
            left[i]=max(left[i-1],prices[i]-minLeft)
        maxRight=prices[-1]
        for i in range(length-2,-1,-1):
            if prices[i]>maxRight:
                maxRight=prices[i]
            right[i]=max(right[i+1],maxRight-prices[i])
        res=0
        for i in range(length):
            print res
            if res<left[i]+right[i]:
                res=left[i]+right[i]
        return res
            


if __name__=='__main__':
    sol=Solution()
    prices=[3,1,2,4,5,7,8]
    print sol.maxProfit(prices)
