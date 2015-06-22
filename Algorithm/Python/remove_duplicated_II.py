class Solution:
    def removeDuplicates(self,A):
        if not A:
            return 0
        slow=0
        flag=0
        for fast in range(1,len(A)):

            if A[fast]==A[slow]:
                flag+=1
                if flag==1:
                    slow+=1
                    A[slow]=A[fast]
                else:
                    continue
                    
            else:
                flag=0
                slow+=1
                A[slow]=A[fast]
        print A[0:slow+1]
        return slow+1
if __name__=='__main__':
    sol=Solution()
    A=[1,1,1,1,1,1,1]    
    print sol.removeDuplicates(A)
