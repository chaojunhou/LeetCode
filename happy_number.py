class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        res = []
        def exract(n):
            lst = []
            while n:
                lst.append(n%10)
                n = n/10
            return lst
        while 1:
            tmp = 0
            
            for i in exract(n):
                tmp += i**2
            if tmp == 1:
                return True
            if tmp in res:
                return False
            res.append(tmp)
            n = tmp

        

if __name__ == '__main__':
    sol = Solution()
    n = 0
    print sol.isHappy(n) 
