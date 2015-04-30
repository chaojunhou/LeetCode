class Solution:
    def search(self,A,target):
        if not A:
            return -1
        
        length=len(A)    
    
        l=0
        r=length-1
        while l<=r:
            mid=(l+r)/2
            print l,r,mid
            if A[mid]==target:
                return mid
            if A[mid]<A[r]: # the right is in order
                if A[mid]<target<=A[r]:
                    l=mid+1
                else:
                    r=mid-1         
            else:  # the left is in order
                if A[l]<=target<A[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
if __name__=='__main__':
    sol=Solution()
    A=[x for x in range(45)]
    from collections import deque
    d=deque(A)
    d.rotate(44)
    A=list(d)
    print A
    

    
    print sol.search(A,3)
