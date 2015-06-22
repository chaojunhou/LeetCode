class Solution:
    def findPeakElement(self,num):
        n = len(num)
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right - left+1)/2
            if (mid == 0 or num[mid-1]<num[mid]) and (mid == n-1 or num[mid] > num[mid+1]):
                return mid
            elif num[mid-1]<num[mid]<num[mid+1]:
                left=mid+1
            else:
                right=mid-1
    def findPeakElement_1(self,num):
        n=len(num)
        return self.find(num,0,n-1)
    def find(self,num,left,right):
        mid=left+(right-left)/2
        if (mid==0 or num[mid-1]<num[mid]) and (mid==len(num)-1 or num[mid+1]<num[mid]):
            return mid
        elif mid>0 and num[mid-1]>num[mid]:
            return self.find(num,left,mid-1)
        else:
            return self.find(num,mid+1,right)

if __name__=='__main__':
    sol=Solution()
    num=[4,1]
    num = [1,3,2,1]
    num = [1]
    num = [1,2]
    print sol.findPeakElement(num)
    print sol.findPeakElement_1(num)
