class Solution:
    def jump(self,A):
        length=len(A)
        reach=0
        jumpNum=0
        while True:
            jumpNum+=1
            for i in range(reach+1):
                if i<=reach:
                    reach=max(reach,A[i]+i)
                if reach>=length-1:
                    return jumpNum
    def jump_1(self,A):
        length=len(A)
        ret=0
        last=0
        curr=0
        for i in range(length):
            if i>last:
                last=curr
                ret+=1
            curr=max(curr,i+A[i])
        return ret
                    

if __name__=='__main__':
    sol=Solution()
    A=[2,3,1,1,4]
    print sol.jump(A)
