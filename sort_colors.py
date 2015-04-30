from random import *
class Solution:
    def sortColors(self,A):
        n=len(A)
        j=n-1
        i=0
        for num in A:
            if num==0:
                i+=1
            elif num==2:
                j-=1
        for x in range(len(A)):
            if x<i:
                A[x]=0
            elif x <=j:
                A[x]=1
            else:
                A[x]=2
            
        '''while i<j:
            if A[i]<A[j]:
                i+=1 
                j-=1
            else:
                A[i],A[j]=A[j],A[i]
                if A[i]>A[0]:    
                    A[i],A[0]=A[0],A[i]
                    i=0
                j-=1
                if A[j]>A[-1]:
                    A[j],A[-1]=A[-1],A[j]
                    j=n-1
                i+=1
                
        while i<j:
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
            if A[i]>A[j]:
                A[i],A[j]=A[j],A[i]
            else:
                i+=1
                j-=1 '''
        
        print 'After:'
        print A

if __name__=='__main__':
    sol=Solution()
    
    A1=[randint(0,2) for x in range(20)]
    A=[1]
    print 'Before:'
    print A
    sol.sortColors(A)
