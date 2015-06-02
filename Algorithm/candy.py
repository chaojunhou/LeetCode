class Solution:
    def candy(self,ratings):
        length=len(ratings)
        cNum=[1 for i in range(length)]
        for i in range(1,length):
            if ratings[i]>ratings[i-1]:
                cNum[i]=cNum[i-1]+1
        for i in range(length-2,-1,-1):
            if ratings[i]>ratings[i+1] and cNum[i]<=cNum[i+1]:
                cNum[i]=cNum[i+1]+1
        return sum(cNum)
if __name__=='__main__':
    sol=Solution()
    ratings=[1,4,3,6,2]
    print sol.candy(ratings)
