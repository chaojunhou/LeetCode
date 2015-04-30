class Solution:
    def isNumber(self,s):
        n=len(s)
        i=0
        while i<n and s[i]==' ':
            i+=1      
        isNumeric=False
        while i<n and s[i].isdigit():
            i+=1
            isNumeric=True
        if i<n and s[i]=='.':
            i+=1
            while i<n and s[i].isdigit():
                i+=1
                isNumeric=True
        if isNumeric and i<n and s[i]=='e':
            i+=1
            if i<n and s[i] in '+-':
                i+=1
            while i<n and s[i].isdigit():
                i+=1
                isNumeric=True
        while i<n and s[i].isspace():
            i+=1
        return isNumeric and i==n
                

if __name__=='__main__':
    sol=Solution() #0e return False
    print sol.isNumber('1.38354e+8')
