import random
class Solution:
    def findKth(self, A):
        pass
    def singleNumber(self, A):
        n = len(A)
        for number in range(n):
            number ^= 0
        return number
    
        


if __name__ == '__main__':
    sol = Solution()
    
    A = [random.randint(1,100) for i in range(10)]
    print A
    print sol.findKth(A)
    print sol.singleNumber(A)
    
