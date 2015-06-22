class Solution:
    def merge(self,A,m,B,n):
        x = m+n
        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                A[x-1] = A[m-1]
                m -=1
            else:
                A[x-1] = B[n-1]
                n -=1
            x -= 1
            
        if n > 0:
            A[:x]=B[:n]
        return
                    
                
            
        


if __name__=='__main__':
    import random
    sol=Solution()
    A=[random.randint(0,100) for x in range(10)]
    A.sort()
    B=[random.randint(0,100) for x in range(10)]
    B.sort()
    print B
    m = len(A)
    n=len(B)
    for x in range(n):
        A.append(0)
    print A
    print len(A)
    sol.merge(A,m,B,n)
