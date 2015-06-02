import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    count +=1
        return count == 1
                
        
if __name__=='__main__':
    sol=Solution()
    nums = [random.randint(1, 10) for i in range(10)]
    k = random.randint(1, 10)
    print nums, k
    print sol.containsNearbyDuplicate(nums,k)
