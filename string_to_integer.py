class Solution:
    def atoi(self,str):
        if len(str)==0:
            return 0
        str=str.strip()
        print str
        sTemp=''
        for index  in range(len(str)):
            
            if str[index] in ('0123456789') or (index==0 and str[index] in ('+','-')):
                sTemp+=str[index]
                print index
            else:
                return 0
        number=int(sTemp)
        if number<=-2147483648:
            return -2147483648
        elif number>=2147483647:
            return 2147483647
        else:
            return number    
if __name__=='__main__':
    sol=Solution()
    print sol.atoi('+004500')
    
                
        
