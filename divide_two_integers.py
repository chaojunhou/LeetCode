class Solution:
    def divide(self,dividend,divisor):
        if dividend>0 and divisor >0:
            sign=1
        elif dividend<0 and divisor<0:
            sign=1
        else:
            sign=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        if dividend<divisor:
            return 0
        else:
        
            result=0
            while dividend>=divisor:
                cont=0
                Temp=divisor
            
                while dividend>=Temp:
                    Temp=Temp<<1
                    cont+=1
            
                
                cont-=1
                
                dividend-=divisor<<cont
                
            
                result+=1<<cont
                
                
                
               
        return sign*result


if __name__=='__main__':
    sol=Solution()
    print sol.divide(32,32)
