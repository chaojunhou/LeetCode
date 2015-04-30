class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res<<1 
            res +=n & 1
            n = n>>1
        return res
            

if __name__ == '__main__':
    sol = Solution()
    n = 43261596
    print sol.reverseBits(n)
