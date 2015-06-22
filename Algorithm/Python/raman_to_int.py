class Solution:
    def romanToInt(self,s):
        numerals={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        s=s[::-1]
        summ=0
        pre=None
        for x in s:
            if pre and numerals[x]<pre:
                summ-=2*numerals[x]
            summ+=numerals[x]
            pre=numerals[x]
        return summ 


if __name__=='__main__':
    sol=Solution()
    print sol.romanToInt('CXCIX')
    
