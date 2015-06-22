class Solution:
    def convert(self,s,nRows):
        if nRows==1:
            return s
        tmp=['' for x in range(nRows)]
        position=-1
        direction=1
        for i in range(len(s)):
            position+=direction
            if position==0:
                direction=1
            elif position==nRows-1:
                direction=-1
            tmp[position]+=s[i]
        return ''.join(tmp)
if __name__=='__main__':
    sol=Solution()
    s='PAYPALISHIRING'
    nRows=3
    print sol.convert(s,nRows)
