class Solution:
    def containDuplicate(self, nums):
        dic = dict.fromkeys(nums,1)
        return len(dic) != len(nums)
