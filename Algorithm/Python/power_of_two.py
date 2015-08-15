class Solution:
    def isPowerOfTwo(self, n):
        return not n&(n-1)


if __name__ == '__main__':
    sol = Solution()
    import random
    n = random.randint(1,20000000)
    
    print n,sol.isPowerOfTwo(n)
    
