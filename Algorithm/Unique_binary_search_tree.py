class Solution:
    def numTrees(self,n):
        if n==0 or n==1:
            return 1     
        else:
            cunt=[0 for i in range(n+1)]
            cunt[0]=1
            cunt[1]=1
            for i in range(2,n+1):
                for j in range(0,i):
                    cunt[i]+=cunt[j]*cunt[i-1-j]
            return cunt[n]
if __name__=='__main__':
    sol=Solution()
    for i in range(10):
        print str(i)+':'+str(sol.numTrees(i))
