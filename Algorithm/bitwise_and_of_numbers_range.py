class Solution:
    def rangeBitwiseAnd(self, m, n):
        if 2*m <= n:
            return 0
        res = m
        for i in range(m+1,n+1):
            res = res&i
            if res == 0:
                return 0
        return res    

    def rangeBit(self,m,n):
        res = m
        for i in range(m+1,n+1):
            res = res&i
        return res


if __name__ == '__main__':
    sol= Solution()
    lst = [(12,14),(6,7),(0,1)]
    for val in lst:
        m = val[0]
        n = val[1]
        print sol.rangeBitwiseAnd(m,n),sol.rangeBit(m,n)
        
