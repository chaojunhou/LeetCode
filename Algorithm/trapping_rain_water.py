class Solution:
    def trap(self,A):
        length=len(A)
        summ=0
        leftmax=0
        left=[0 for i in range(length)]
        for i in range(length):
            if leftmax<A[i]:
                leftmax=left[i]=A[i]
            else:
                left[i]=leftmax
        right=0
        print left
        for i in range(length-1,-1,-1):
            if A[i]>right:
                right=A[i]
            summ+=min(left[i],right)-A[i]
        return summ

if __name__=='__main__':
    sol=Solution()
    print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
