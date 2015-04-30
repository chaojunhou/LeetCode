import unittest
class Solution(unittest.TestCase):
    def test_fractionToDecimal(self):
        self.assertEqual(self.fractionToDecimal(1,3),'0.(3)')
        self.assertEqual(self.fractionToDecimal(1,5),'0.2')
    def fractionToDecimal(self, numerator, denominator):
        sign=numerator*denominator
        result=''
        if sign<0:
            result+='-'
        elif sign==0:
            return '0'
        count=0
        numerator=abs(numerator)
        denominator=abs(denominator)
        if numerator>=denominator:
            count=numerator/denominator
            numerator=numerator%denominator
        if numerator==0:
            result+=str(count)
            return result
        else:
            result+=str(count)+'.'
        tmp=[]
        while 1:
            numerator*=10
            if numerator in tmp:
                result+=')'
                offset=tmp.index(numerator)
                start=result.find('.')
                position=start+offset+1
                result=result[:position]+'('+result[position:]
                return result
            else:
                tmp.append(numerator)
                result+=str(numerator/denominator)               
                numerator=numerator%denominator
                if numerator==0:
                    return result
if __name__=='__main__':
    unittest.main()
