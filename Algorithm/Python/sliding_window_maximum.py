import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow1(self, nums, k):
        if not nums:
            return []
        n = len(nums)
        deq = collections.deque(nums[:k])
        res =[]
        Max = max(deq)
        res.append(Max)
        for i in range(k, n):
            deq.popleft()
            deq.append(nums[i])
            if nums[i] > Max:
                Max = nums[i]
            else:
                Max = max(deq)
            res.append(Max)
        return res  
    def maxSlidingWindow(self, nums, k):                        
        if nums == []:
            return []
        ans,tmp = [], []
        for i in range(0, k):
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
            
        for i in range(k, len(nums)):
            ans.append(nums[tmp[0]])
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
            print tmp
            while tmp != [] and tmp[0] <= i-k:
                tmp.pop(0)
            print tmp
        ans.append(nums[tmp[0]])
        return ans
                
        



if __name__ == '__main__':
    sol = Solution()
   
    nums = [1, 3, -1,-3,5,3,6,7]
    k = 3
    print sol.maxSlidingWindow(nums, k)
    '''
    nums = [1,-1]
    k = 1
    print sol.maxSlidingWindow(nums, k)
    nums = [2,4,7]
    k = 2
    print sol.maxSlidingWindow(nums,k)
    nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
    k = 7
    print sol.maxSlidingWindow(nums,k)
    
    nums = [1,3,1,2,0,5]
    k=3
    print sol.maxSlidingWindow(nums,k)
    '''
