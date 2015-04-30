class Solution:
    def searchInsert(self,A,target):
        if A :
            if A[0]>target:
                return 0
            elif A[-1]<target:
                return len(A)
            else:
                i=0
                while A[i]<=target:
                    i+=1
                return i
        else:
            return 0
    def searchInsert1(self, A, target):
        length = len(A)
        if length ==0:
            return 0
        left, right = 0, length-1
        while left < right :
            mid = (right - left)/2 + left
            if A[mid] > target:
                right = mid -1
            else:
                left = mid
        return left+1 if A[left] < target else left
if __name__=='__main__':
    sol=Solution()
    #A=[1,3,5,6]
    #target=5
    A = [1,3]
    target = 1
    print sol.searchInsert(A,target)
    print sol.searchInsert1(A,target)
