class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        pre = 0
        total = 0
        for c in s:
            cur = numerals[c]
            if pre < cur:
                total += cur -2*pre
            else:
                total += cur
            pre = cur
        return total
            
if __name__ == '__main__':
    sol = Solution()
    print sol.romanToInt('MXCVI')
