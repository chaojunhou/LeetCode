class Solution:
    def canJump(slef,A):
        length=len(A)
        reach=0
        for i in range(length):
            if i<=reach:
                reach=max(reach,A[i]+i)
        if reach>=length-1:
            return True
        else:
            return False
            
if __name__=='__main__':
    sol=Solution()
    A=[0,1]
    print sol.canJump(A)
