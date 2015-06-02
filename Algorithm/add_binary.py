class Solution:
    def addBinary(self,a,b):
        length_a=len(a)
        length_b=len(b)
        
        if length_a>length_b:
            b='0'*(length_a-length_b)+b
            max_length=length_a
        else:
            a='0'*(length_b-length_a)+a
            max_length=length_b
        carry=0
        c=[]
        for index in range(max_length-1,-1,-1):
            if a[index]=='0':
                x=0
            else:
                x=1
            if b[index]=='0':
                y=0
            else:
                y=1
            tmp=x+y+carry
            carry=tmp/2
            c.insert(0,tmp%2)
        
        if carry==1:
            c.insert(0,1)
        stp=''.join(str(element) for element in c )
        return stp
            



if __name__=='__main__':
    sol=Solution()
    a='110'
    b='110'
    print sol.addBinary(a,b)
