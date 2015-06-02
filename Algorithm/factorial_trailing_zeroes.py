class Solution:
    def trailingZeroes(self,n):
        count=0
        while n>0:
            n=n/5
            count+=n
        return count
            
if __name__=='__main__':
    sol=Solution()
    print sol.trailingZeroes(10);
