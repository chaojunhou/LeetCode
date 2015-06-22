class Solution:
    def isScramble(self,s1,s2):
        if s1==s2:
            return True
        length=len(s1)
        if length!=len(s2):
            return False
        if sorted(s1)!=sorted(s2):
            return False
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]):
                return True
        return False
if __name__=='__main__':
    sol=Solution()
    s1='great'
    s2='rgtae'
    print sol.isScramble(s1,s2)
