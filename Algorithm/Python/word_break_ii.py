class Solution:
    def wordBreak(self,s,dict):
        self.res=[]
        self.dfs(s,dict,'')
        return self.res
    def check(self,s,dict):
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i]=True
        return dp[len(s)]
    def dfs(self,s,dict,sList):
        if self.check(s,dict):
            if len(s)==0:
                self.res.append(sList[1:])
            for i in range(1,len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:],dict,sList+' '+s[:i])
        


if __name__=='__main__':
    sol=Solution()
    s='catsanddog'
    dict=['cat','cats','and','sand','dog']
    print sol.wordBreak(s,dict)
