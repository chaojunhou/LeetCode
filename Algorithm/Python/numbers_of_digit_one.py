class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne1(self, n):
        def countNumber(n):
            count = 0
            while n != 0:
                if n%10 == 1:
                    count += 1
                n = n/10
            return count
        ans = 0
        for i in range(1,n+1):
            ans += countNumber(i)
        return ans
    def countDigitOne(self, n):
        iCount, iFactor, iLowerNum, iCurrNum, iHigherNum = 0, 1, 0, 0, 0
        while n/iFactor:
            iLowerNum = n - (n/iFactor)* iFactor
            iCurrNum = (n / iFactor)%10
            iHigherNum = n/(iFactor*10)

            if iCurrNum == 0:
                iCount += iHigherNum * iFactor
            elif iCurrNum == 1:
                iCount += iHigherNum * iFactor + iLowerNum +1
            else:
                iCount += (iHigherNum + 1) * iFactor
            iFactor *= 10
        return iCount


if __name__ == '__main__':
    sol = Solution()
    n = 3184191
    print sol.countDigitOne1(n)
