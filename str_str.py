class Solution:
    def kmp_match(self,haystack,needle):
        n=len(haystack)
        m=len(needle)
        prefix=self.compute_prefix(needle)
        j = -1        
        for i in range(n):
            while j > -1 and needle[j+1]!=haystack[i]:
                j = prefix[j] 
            if needle[j+1] == haystack[i]:
                j = j+1
            if j == m-1:
                return i+1-m
                #j = prefix[j] find more possible position
        return -1
    def compute_prefix(self,P):
        m=len(P)
        prefix=[-1 for i in range(m)]
        j = -1
        for i in range(1,m):
            while j > -1 and P[j+1]!=P[i]:
                j=prefix[j]
            if P[j+1]==P[i]:
                j+=1
            prefix[i]=j
        return prefix
    
    def strStr(self, haystack, needle):
        n=len(haystack)
        m=len(needle)
        if haystack==needle:
            return 0
        if n<m:
            return -1
        for x in range (n-m+1):
            if haystack[x:m+x]==needle:
                return x
        return -1 
if __name__=='__main__':
    sol=Solution()
    T='bacbababaabcbab'
    P=''
    print sol.strStr(T,P)
    print sol.kmp_match(T,P)
            
        
