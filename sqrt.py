class Solution:
    def sqrt (self, x ):
        t = 1
        while 1:
            if t**2 == x or (t**2 < x and (t+1)**2 > x):
                return t
            t = (t + x/t)/2
    def sqrt1(self,x):
        low=0
        high=x/2+1
        while low<=high:
            mid=(low+high)/2
            if mid**2<=x<(mid+1)**2:
                return mid
            elif mid**2<x:
                low=mid+1
            else:
                high=mid-1
if __name__ == '__main__':
    sol = Solution()
    print sol.sqrt(10000)
