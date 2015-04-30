class Solution:
    def findPeakElement(self,num):
        left=0
        right=len(num)-1
        if right<3:
            return num.index(max(num))
        while left<=right:
            mid=(left+right)/2
            if mid==left==right:
                return mid
            if num[mid-1]<num[mid] and num[mid]>num[mid+1]:
                return mid
            elif num[mid-1]<num[mid]<num[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return 1
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
    num=[1,2,3,4]
    print sol.findPeakElement(num)
    print sol.findPeakElement_1(num)
