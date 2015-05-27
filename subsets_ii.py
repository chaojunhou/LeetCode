class Solution:
    def subsetsWithDup(self, nums):
        self.res=[]
        nums.sort()
        n = len(nums)
        self.dfs(0,0,n,[],nums)
        return self.res
    
    def dfs(self,depth,start,n, ans, nums):
        self.res.append(ans)
        if depth == n:
            return
        pre = -2<<10
        for index in range(start, n):
            if pre != nums[index]:
                self.dfs(depth+1,index+1, n, ans+[nums[index]], nums)
                pre = nums[index]   


if __name__=='__main__':
    sol=Solution()
    S=[1,2,2]
    print sol.subsetsWithDup(S)
