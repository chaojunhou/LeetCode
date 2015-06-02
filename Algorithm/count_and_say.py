class Solution:
    def countAndSay(self,n):
        word='1'
        for x in range(n-1):
            pre=''
            stemp=''
            num=1
            for element in word:
                if element==pre:
                    num+=1
                elif pre!='':
                    stemp+=str(num)+pre
                    num=1
                pre=element
            stemp+=str(num)+pre
            word=stemp                 
        return word
        

    
if __name__=='__main__':
    sol=Solution()
    sol.countAndSay(2)
    for x in range(1,10):
        print sol.countAndSay(x)
