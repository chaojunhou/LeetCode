class Solution:
    def rob(self,nums):
        print nums[:-1]
        return max(self.robber(nums[:-1]),self.robber(nums[1:]))
    def robber(self,nums):
        length = len(nums)
        if length < 2:
            return nums[0] if nums else 0
        dp = [0 for x in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return  dp[length-1]
    def rob1(self, nums):
        length = len(nums)
        if length < 2:
            return nums[0] if nums else 0
        dp = [0 for x in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        if dp[length-3]+nums[length-1] > dp[length-2]:
            return dp[length-2]
        else:
            return dp[length-1] 


if __name__ == '__main__':
    sol = Solution()
    #nums = [1,1,1,1]
    #nums = [2,3,2]
    nums = [1,2,1,1]
    print sol.rob1(nums)
