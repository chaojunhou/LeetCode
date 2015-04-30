class Solution:
    def titleToNumber(self,s):
        result=0
        for char in s:
            result=26*result+ord(char)-64
        return result
            
if __name__=='__main__':
    s='Z'
    sol=Solution()
    print sol.titleToNumber(s)
