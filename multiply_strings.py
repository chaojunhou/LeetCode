class Solution:
    def multiply(self,num1,num2):
        length1=len(num1)
        length2=len(num2)
        digits=[0 for x in range(length1+length2)]
        num1=num1[::-1]
        num2=num2[::-1]
        for index1 in range(length1):
            for index2 in range(length2):
                digits[index1+index2]+=int(num1[index1])*(int(num2[index2]))

        carry=0
        Str=''
        length=len(digits)
        for index in range(length):
            remainder=digits[index]%10
            carry=digits[index]/10
            if index<length-1:
                digits[index+1]+=carry
            Str+=str(remainder)
          
        Str=Str[::-1]
        
        i=0
        while Str[i]=='0' and length-1>i:
            i+=1
        return Str[i:]
            
            
            


if __name__=='__main__':
    sol=Solution()
    num1='9'
    num2='99'
    print sol.multiply(num1,num2)
