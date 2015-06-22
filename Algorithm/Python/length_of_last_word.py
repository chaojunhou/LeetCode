class Solution:
    def lengthOfLastWord(self,s):
        lst=[]
        for word in s.split(' '):
            lst.append(word)
        for word in lst[::-1]:
            if len(word)>0:
                return len(word)
        return 0
     
if __name__=='__main__':
    sol=Solution()
    print sol.lengthOfLastWord('a ')
