class Solution:
    def plusOne(self,digits):
        carry=1
        for number in range(len(digits)-1,-1,-1):
            digits[number]+=carry
            carry=digits[number]/10
            digits[number]%=10
            if carry==0:
                break
        if carry==1:
            digits.insert(0,1)
        return digits
    def plusOne1(self,digits):
        length = len(digits)
        for i in range(length-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0 
        digits.append(0)
        digits[0]=1
        return digits

if __name__ =='__main__':
    sol=Solution()
    import random
    digits=[random.randint(0,9) for x in range(10)]
    print digits
    print sol.plusOne1(digits)
