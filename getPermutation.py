class Solution:
    def getPermutation(self,n,k):
        res=''
        cur=[x for x in range(1,n+1)]
        print cur
        k-=1
        for cont in range(n-1,-1,-1):
            res+=str(cur[k/self.factorial(cont)])           
            cur.remove(cur[k/self.factorial(cont)])
            k=k%self.factorial(cont)
        return res
            
    def factorial(self,n):
        if n<=1:
            return 1
        fac=1
        for x in range(1,n+1):
            fac*=x
        return fac

if __name__=='__main__':
    sol=Solution()
    print sol.getPermutation(4,4)
