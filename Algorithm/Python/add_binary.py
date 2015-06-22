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
    def addBinary1(self,a,b):
        self.res = ''
        if len(a) < len(b):
            return self.add(b,a)
        return self.add(a,b)
        
    def add(self,a,b):
        # length of a is larger than b now
        n = len(b)
        flag = 0
        k = len(a) - n
        for i in range(n-1,-1,-1):
            ai = int(a[i+k])
           
            bi = int(b[i])          
            self.res += str(ai^bi^flag)
            flag  = (ai+bi+flag)/2
        for i in range(k-1,-1,-1):
            ai = int(a[i])
            self.res += str((ai+flag)%2)
            flag = ai&flag;
        if flag:
            self.res +='1'
        return self.res[::-1]
            
            


if __name__=='__main__':
    sol=Solution()
    a='1111110'
    b='101111'

    print sol.addBinary(a,b)
    print sol.addBinary1(a,b)
