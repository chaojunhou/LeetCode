class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        if n<m:
            return -1
        print n,m
        for x in range (n-m+1):
            print haystack[x:m+x],needle
            if haystack[x:m+x]==needle:
                return x                
        return -1
    def 
            

if __name__=='__main__':
    sol=Solution()
    haystack='mississippi'
    needle='pi'
    print sol.strStr(haystack,needle)
