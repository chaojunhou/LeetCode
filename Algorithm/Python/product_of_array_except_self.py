class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        res = 1
        counter = 0
        for num in nums:
            if num != 0:
                res *= num
            else:
                counter += 1
        if counter > 1:
            return [0 for num in nums]
        elif counter == 1:
            ans = []
            for num in nums:
                if num == 0:
                    ans.append(res)
                else:
                    ans.append(0)
            return ans  
        else:
            return [res/num for num in nums]
            


if __name__ == '__main__':
    sol = Solution()
    import random
    nums = [random.randint(0,10) for i in range(6)]
    print nums
    print sol.productExceptSelf(nums)
