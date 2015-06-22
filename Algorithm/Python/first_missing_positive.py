class Solution:
    def firstMissingPositive(self,A):
        index=0
        n=len(A)
        while index<n:
            if A[index]>0 and A[index]<=n and A[index]!=(index+1) and A[A[index]-1]!=A[index]:
                A[A[index]-1], A[index]=A[index],A[A[index]-1]
            else:
                index+=1
        for x in range(n):
            if A[x]!=x+1:
                return x+1
        return n+1

    def firstMissingPositive1 (self, A):
        n = len(A)
        for i in range(n):
            while  A[i]>0 and A[i]<= n  and A[i] != A[A[i]-1] :
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
        for x in range(n):
            if A[x]!=x+1:
                return x+1
        return n+1


if __name__=='__main__':
    sol=Solution()
    A=[-1,4,2,1,9,10]
    A = [3,4,-1,1]
    B =  A[:]
    print sol.firstMissingPositive(A)
    print B
    print sol.firstMissingPositive1(B)

