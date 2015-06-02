class Solution:
    def generateParenthesis(self,n):
        self.res=[]
        self.dfs(0,0,'',n)
        return self.res
    def dfs(self,l,r,ans,n):
        if r>n or l>n:
            return 
        if l==n and r==n:
            self.res.append(ans)
        if l>r:
            self.dfs(l,r+1,ans+')',n)
        if l<n:
            self.dfs(l+1,r,ans+'(',n)
        
            


if __name__=='__main__':
    sol=Solution()
    print sol.generateParenthesis(1)
