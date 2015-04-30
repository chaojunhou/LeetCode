class Solution:
    def sqrt (self, x ):
        t = 1
        while 1:
            if t**2 == x or (t**2 < x and (t+1)**2 > x):
                return t
            t = (t + x/t)/2
if __name__ == '__main__':
    sol = Solution()
    print sol.sqrt(10000)
