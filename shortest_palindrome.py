class Solution:
       
    def shortestPalindrome(self, s):
        haystack = s[::-1]
        m = len(s)
        j = -1
        prefix=self.compute_prefix(s)
        for i in range(m):
            while j > -1 and s[j+1]!=haystack[i]:
                j = prefix[j]
            if s[j+1] == haystack[i]:
                j = j+1
        return s[m-1:j:-1]+s
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
    def shortestPalindrome1(self, s):
        if self.isPalindrome(s):
            return s
        n = len(s)        
        for i in range(n-2,-1,-1):
            if self.isPalindrome(s[:i]):
                break
        return s[n-1:i-1:-1]+s
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left<right:
            if  s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True     

if __name__ == "__main__":
    sol = Solution()
    s = "abbacd"
    print sol.shortestPalindrome1(s)
