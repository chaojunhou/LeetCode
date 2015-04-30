class Solution:
    def longestPalindrome (self, s):
        length = len(s)
        def expand(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -=1
                right +=1
            return right - left -1
            
        start, end = 0, 0
        for  i in range(length):
            len1 = expand(i,i)
            len2 = expand(i,i+1)
            Len = max (len1, len2)
            if end - start < Len:
                start = i - (Len-1)/2 // for the even palindrome
                end = i + Len/2
        return s[start:end+1]



if __name__ == '__main__':
    s = 'bb'
    sol =Solution()
    print sol.longestPalindrome(s)
