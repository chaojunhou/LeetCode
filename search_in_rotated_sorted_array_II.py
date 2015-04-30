class Solution:
    def search(self,A,target):
        if not A:
            return False
        
        length=len(A)    
    
        l=0
        r=length-1
        while l<=r:
            mid=(l+r)/2
            print l,r
            if A[mid]==target:
                return True
            if A[mid]<A[r]: # the right is in order
                if A[mid]<target<=A[r]:
                    l=mid+1
                
                else:
                    r=mid-1         
            elif A[mid]>A[r]:  # the left is in order
                if A[l]<=target<A[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                r-=1
                
        return False
if __name__=='__main__':
    sol=Solution()
    import random
    A=[random.randint(0,45) for x in range(20)]
    A.sort()
    from collections import deque
    d=deque(A)
    d.rotate(44)
    A=list(d)
    A=[1,1,3,1]
    print A
       
    print sol.search(A,3)
