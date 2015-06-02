class Solution:
    def reverse(self,x):

        lst=[]
        while x/10!=0:
            lst.append(x%10)
            x=x/10

        lst.append(x)
        number=1

        for x in range(len(lst)):
            number=number*10+x

        return number
if __name__=='__main__':
    sol=Solution()
    
    print sol.reverse(123)
        
