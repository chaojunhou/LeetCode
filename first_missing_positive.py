class Solution:
    def firstMissingPositive(self,A):
        index=0
        length=len(A)
       
        while index<length:
            if A[index]!=(index+1) and A[index]>=1 and A[index]<=length and A[A[index]-1]!=A[index]:
                
                A[A[index]-1], A[index]=A[index],A[A[index]-1]
                
            else:
                index+=1
               
        for x in range(length):
            if A[x]!=x+1:
                return x+1
        return n+1
    def first(self,A):
        n=len(A)
        index=0
        while index<n:
            
            if A[index]>0 and A[index]<=n:
                if A[index]!=A[A[index]-1]:
                    A[A[index]-1],A[index]=A[index],A[A[index]-1]
                    
                else:
                    index+=1
                     
        for x in range(n):
            if A[x]!=x+1:
                return x+1
        return n+1
        
    
        

if __name__=='__main__':
    sol=Solution()
    A=[-1,4,2,1,9,10]
    #print sol.firstMissingPositive(A)
    print sol.first(A)
