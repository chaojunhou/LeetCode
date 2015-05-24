class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        self.res = []
        self.dfs(k, n, 0)
        return self.res
    
    def dfs(self, k, n, start, tmp=[]):
        if n < 0:
            return
        elif n ==0 and k == 0:
            self.res.append(tmp[:])
        else:
            pre = -1
            for i in range(start+1,10):
                if n < i:
                    return
                if pre != i:
                    self.dfs(k-1, n-i, i, tmp + [i])
                    pre = i
            
        


if __name__ == '__main__':
    sol = Solution()
    k = 3
    n = 7
    print sol.combinationSum3(k,n)
