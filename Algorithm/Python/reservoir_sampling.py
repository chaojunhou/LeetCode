class Solution:
    def reservoir_sampling(self,A,k):
        import random
        R=[A[x] for x in range(k)]
        for i in range(k+1,len(A)):
            j=random.randint(1,i)
            if j<k:
                R[j]=A[i]
        return R

if __name__=='__main__':
    sol=Solution()
    import random
    A=[random.randint(1,100) for x in range(10,20)]
    print A
    print sol.reservoir_sampling(A,5)
            
