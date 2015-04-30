class Solution:
    def isPalindrome(self,s):
        left=0
        right=len(s)-1
        s=s.lower()
        while left<right:
            while not s[left].isalnum():
                left+=1
                if left==len(s):
                    return True
            while not s[right].isalnum():
                right-=1
                if right<left:
                    print 'fuck'
                    return True
            if s[left].isalnum() and s[right].isalnum() and s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True    


if __name__=='__main__':
    sol=Solution()
    print sol.isPalindrome('Sue," Tom smiles, "Selim smote us.')
