class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        def getRange(begin, end):
            return str(begin)+"->" + str(end) if begin != end else str(begin)
        n = len(nums)
        if n == 0:
            return []
        res = []
        pre = start = nums[0]
        for num in nums:
            cur = num 
            if cur - pre > 1:
                res.append(getRange(start, pre))
                start = cur
            if cur == nums[-1]:
                res.append(getRange(start, cur))
            pre = cur
        return res
                
        



if __name__ == '__main__':
    nums = [0,1,2,3,4,5,6]
    sol = Solution()
    print sol.summaryRanges(nums)
