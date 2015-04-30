class Bitmap(object):
    def __init__(self, max):
        self.size  = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]
 
    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 32 - 1) / 32) #向上取整
        return num / 32
 
    def calcBitIndex(self, num):
        return num % 32
 
    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem      = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)
 
    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem      = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))
 
    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return 1
        return 0
    
class Solution:
    def countPrimes2(self, n):
        #from bitarray import bitarray
        if 2 >= n:
            return 0
        #size = int((n+31-1)/31)
        #a = [1 for i in xrange(n)]
        bitmap = Bitmap(n)
        for i in range(n):
            if i%2 == 0:
                bitmap.set(i)
        bitmap.set(1)
        bitmap.clean(2)
        sn = int(n**0.5)
        for i in xrange(3,sn+1,2):
            if  not bitmap.test(i):
                for j in xrange(i<<1,n,i):
                    bitmap.set(j)
        count = 0
        
        
        for i in range(n):
            if not bitmap.test(i):
                count +=1
       
        return count
    def countPrimes(self, n):
        from bitarray import bitarray
        if 2 >= n:
            return 0
        #size = int((n+31-1)/31)
       # a = [1 for i in xrange(n)]
        a = [True]*n
        for i in range(n):
            if i%2 == 0:
                a[i] = False
        a[1] = False
        a[2] = True
        sn = int(n**0.5)
        for i in xrange(3,sn+1,2):
            if  a[i]:
                for j in xrange(3*i,n,i<<1):
                    a[j] = False
        return sum(1 for val in a if val)
    
    def countPrimes1(self,n):
        def isPrime(n):  
            if n <= 1:  
                return 0 
            if n == 2:  
                return 1 
            if n % 2 == 0:  
                return 0 
            i = 3 
            while i * i <= n:  
                if n % i == 0:  
                    return 0 
                i += 2 
            return 1            
        count = 1
        n += 1
        i = 3
        while  i < n:
            if isPrime (i):
                count +=1
            i += 2
        return count
              


if __name__ == '__main__':
    from time import time
    sol = Solution()
    n=5000000
    t = time()
    print sol.countPrimes(n)
    print time() - t
