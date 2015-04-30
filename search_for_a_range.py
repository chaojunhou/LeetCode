class Solution:
    def searchRange(self,A,target):
        res=[-1,-1]
        if not A:
            return res
        length=len(A)
        ll=0
        lr=length-1
        while ll<=lr:
               # find the left 
            mid=(ll+lr)/2
            
            if A[mid]==target:
                break
            elif A[mid]<target:
                ll=mid+1
            else:
                lr=mid-1
        if ll>lr:
            return res
        while A[ll]!=target:
            ll+=1
        rl=ll
        rr=lr
        while rl<=rr:
        
            if A[rr]>target:
                
                rr-=1                
            elif A[rl]<target:
    
                 rl+=1
            else:
                break
        res[0]=rl
        res[1]=rr
        return res
    def searchRange_1(self,A,target):
        res=[-1,-1]
        if not A:
            return res
        length=len(A)
        ll=0
        lr=length-1
        while ll<=lr:
            mid=(ll+lr)/2
            if A[mid]<target:
                ll=mid+1
            else:
                lr=mid-1
        rl=0
        rr=length-1
        while rl<=rr:
            mid=(rl+rr)/2
            if A[mid]<=target:
                rl=mid+1
            else:
                rr=mid-1
        if ll<=rr:
            res[0]=ll
            res[1]=rr
        return res
    def searchRange_2(self,A,target):
        res=[-1,-1]
        if not A:
            return res
        n=len(A)
        left=0
        right=n-1
        while left<=right:
            mid=left+(right-left)/2
            print mid
            if A[mid]==target:
                break
            elif A[mid]<target:
                left=mid+1
            else:
                right=mid-1
        print left,right
        if left>right:
            return res
        while A[left]!=target:
            left+=1
        while A[right]!=target:
            right-=1
        if left<=right:
            res[0]=left
            res[1]=right
        return res
            
if __name__=='__main__':
    sol=Solution()
    import random
    #A=[random.randint(0,100000) for x in range(1000000)]
    #A.sort()
    A=[1,4]
    target=4
    print sol.searchRange_2(A,target)
   
    """
    import time
    start=time.clock()
    sol.searchInsert(A,target)
    second=time.clock()
    print second-start
    second=time.clock()
    sol.searchInsert_1(A,target)
    print time.clock()-second"""
