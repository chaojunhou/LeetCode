import random
class Solution: 
    def findMin(self, num):
        length=len(num)
        if length < 10:       
            return min(num)
        else:
            midLength=length/2
            if num[-1]>num[midLength]:  # delete the right sorted array
                return self.findMin(num[:midLength+1])
            else:
                return self.findMin(num[midLength:])
    def findMin1(self, num):
        n = len(num)
        left, right = 0, n-1
        while left < right and num[left] > num [right] :
            mid = left + (right-left)/2
            if num[mid] <= num[right]:
                right  = mid
            else:
                left = mid+1

        return num[left]
                

if __name__ == '__main__':
    sol = Solution()
    A=[random.randint(1,20) for x in range(10)]
    A = list(set(A))
    from collections import deque
    d=deque(A)
    d.rotate(random.randint(1,7))
    A=list(d)
    B = A
    print A
    print sol.findMin(A)
    print B
    print sol.findMin1(B)
