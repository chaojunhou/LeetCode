class Solution:
    def partition(self,s):
        self.res=[]
        self.dfs(s,[])
        return self.res
    def isPal(self,s):
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def dfs(self,s,ans):
        if len(s)==0:
            self.res.append(ans)
        for i in range(1,len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:],ans+[s[:i]])
        

if __name__=='__main__':
    sol=Solution()
    s='aab'
    print sol.partition(s)
    
