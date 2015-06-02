class Solution:
    def rotate(self,nums,k):
        def rev(num,begin,end):
            left = begin
            right = end
            while left < right:
                num[left],num[right-1] = num[right-1],num[left]
                left +=1
                right -=1
            else:
                return 
        length=len(nums)
        k = k%length
        rev(nums,0,length)
        rev(nums,0,k)
        rev(nums,k,length)
    def rotate_1(self,nums,k):
        print nums
        length = len(nums)
        k = k%length
        nums[:] = nums[-k:] + nums[:-k]
        print nums
        
  

        


if __name__ == '__main__':
    sol=Solution()
    nums=[1,2,3,4,5,6,7]
    k=3
    sol.rotate_1(nums,k)
