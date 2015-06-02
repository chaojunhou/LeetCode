import random
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        if n==1:
            return nums[0]
        q = random.randint(0,n-1)
        nums[-1], nums[q] = nums[q], nums[-1]
        pivort = nums[-1]
        i = -1
        for j in range(n-1):
            if nums[j] <= pivort:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[-1] = nums[-1], nums[i+1]
        cnt =n- i-1
        if cnt == k:
            return pivort
        if cnt > k:           
            return self.findKthLargest(nums[n-cnt+1:], k)
        elif cnt < k:
            return self.findKthLargest(nums[:n-cnt],k-cnt)
        
if __name__ == '__main__':
    sol = Solution()
    nums = [2,1]
    print sol.findKthLargest(nums,2),1
    print '-'*19
    nums = [-1,-1]
    print sol.findKthLargest(nums,2),-1
    print '-'*19
    nums = [7,6,5,4,3,2,1]
    print sol.findKthLargest(nums,5),3
    nums = [3,2,3,1,2,4,5,5,6]
    print '-'*19
    print sol.findKthLargest(nums,9),1
    print '-'*19
    nums= [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    print sol.findKthLargest(nums,20),2
    print '-'*19
    nums= [3,2]
    print sol.findKthLargest(nums,2),2
    print '-'*19
    for i in range(1,7):
        nums = [3,2,1,5,6,4]
        print sol.findKthLargest(nums,i)
                
            
        
        
