class Solution:
    def longestPalindrome(self,s):
        length=len(s)
        if length<2:
            return s
        left=0
        right=0
        s=s.lower()
        maxLen=0
        dp=[[False for x in range(length)] for y in range(length)]
         
        for i in range(length):
            for j in range(length):
                if i>=j:
                    dp[i][j]=True       
        for k in range(1,length):
            for i in range(length-k):
                j=i+k
                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    dp[i][j]=dp[i+1][j-1]
                    if dp[i][j]:
                        if k +1>maxLen:
                            maxLen=k+1
                            left=i
                            right=j
                          
        return s[left:right+1]
    def longestPalindrome_1(self,s):
        length=len(s)
        if length<2:
            return s
        start,maxLen=0,0
        for i in range(1,length):
            low=i-1
            high=i
            while low>=0 and high<length and s[low]==s[high]:
                low-=1
                high+=1

            if high-low-1>maxLen:
                maxLen=high-low-1
                start=low+1
            low=i-1
            high=i+1
            while low>=0 and high<length and s[low]==s[high]:
                low-=1
                high+=1
            if high-low-1>maxLen:
                maxLen=high-low-1
                start=low+1
        return s[start:start+maxLen]
    def longestPalindrome_2(self,s):
        length=len(s)
        if length<2:
            return s
        palindrome=''
        for i in range()
        


if __name__=='__main__':
    sol=Solution()
    s='abb'
    print sol.longestPalindrome(s)
    print sol.longestPalindrome_1(s)
