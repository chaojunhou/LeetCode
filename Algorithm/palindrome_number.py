class Solution:
    def isPalindrome(self,x):
        if x<0:
            return False
        div=1
        while x/div:
            div*=10
        div/=10
        while x and div:
            print x,div
            l=x/div
            r=x%10
            print l,r
            if l!=r:
                return False
            
            x-=l*div+r
            x/=10
            div/=100
        return True
if __name__=='__main__':
    sol=Solution()
    print sol.isPalindrome(2023883202)
                
