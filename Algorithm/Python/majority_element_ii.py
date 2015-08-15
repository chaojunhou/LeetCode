class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        n = len(nums)
        candidate1, candidate2= -1,-1
        count1, count2 = 0, 0
        for i in range(n):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = nums[i]
                count1 = 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        count1, count2 = 0,0
        for i in range(n) :
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
        if count1 > n/3:
            ans.append(candidate1)
        if count2 > n/3:
            ans.append(candidate2)
        return ans  
        
    def test(self, nums):
        return self.majorityElement(nums)
                
            
            
if __name__ == '__main__':
    sol = Solution()
    print sol.test([1,2,2,])
    print sol.test([1,2,3])
    print sol.test([2,1,2,1])
    print sol.test([2,2,2,1,3])
