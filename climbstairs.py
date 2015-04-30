class Solution:
    def climbStairs(self,n):
        if n<4:
            return n
        else:
            stair_1=1
            stair_2=2
            number=0
            count=2
            while count<n:
                number=stair_1+stair_2
                stair_1=stair_2
                stair_2=number
                count+=1
            return number
                 
                 
if __name__=='__main__':
    sol=Solution()
    for x in range(20):
        print sol.climbStairs(x)
