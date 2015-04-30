class Solution:
    def convertToTitle(self,num):
        result=''
        while num!=0:
            tmp=(num-1)%26
            result+=chr(tmp+65)
            num=(num-1)/26                
        return result[::-1]
    def convertToTitle_1(self,num):
        while fraction<num:
            fraction*=26
        fraction/=26
        print fraction
        while fraction!=0:
            tmp=num/fraction
            result+=chr(tmp+64)
            num-=tmp*fraction
            fraction/=26
        return result

if __name__=='__main__':
    sol=Solution()
    print sol.convertToTitle(1)
