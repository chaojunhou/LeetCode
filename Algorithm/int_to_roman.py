class Solution:
    def intToRoman(self,num):
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res=''
        for value in values:
            while num>=value:
                num-=value
                res+=numerals[values.index(value)]
            
        return res

if __name__=='__main__':
    sol=Solution()
    for x in range(41):
        
        print sol.intToRoman(x)
                
