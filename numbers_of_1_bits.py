class Solution:
    def hammingWeight (self,n):
        ans = 0
        for i in range(32):
            if n & 1 :
                ans +=1
            n = n >> 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 11
    print sol.hammingWeight (n)
