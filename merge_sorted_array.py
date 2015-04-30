class Solution:
    def merge(self,A,m,B,n):
        s=m-1
        t=n-1
        x=m+n-1
        while s>-1 and t>-1:
            
            if A[s]>B[t]:
                A[x]=A[s]
                s-=1
            else:
                A[x]=B[t]
                t-=1
            x-=1
        
        if s>-1:
            A[0:x+1]=B[0:t+1]
        print A

        
        '''if m>0:
            
            for x in B:    
                i=0
                while A[i]<x:
                    i+=1
                    if i==len(A):
                        break  
                A.insert(i,x)
        else:
            for y in range(n):
                A.insert(y,B[y])
        print A''' 
                    
                
            
        


if __name__=='__main__':
    import random
    sol=Solution()
    A=[random.randint(0,100) for x in range(10)]
    print len(A)
    A.sort()
    print A
    m=len(A)
    B=[random.randint(0,100) for x in range(10)]
    B.sort()
    print B
    n=len(B)
    for x in range(n):
        A.append(0)
    print A
    
    sol.merge(A,m,B,n)
