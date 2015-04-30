class Solution:
    def minCut(self,s):
        length=len(s)
        if length==0:
            return 0
        dp=[0 for x in range(length+1)]
        p=[[False for x in range(length)] for y in range(length)]
        for i in range(length+1):
            dp[i]=length-i
        for i in range(length-1,-1,-1):
            for j in range(i,length):
                if s[i]==s[j] and (j-i<2 or p[i+1][j-1]):
                    p[i][j]=True
                    dp[i]=min(dp[i],dp[j+1]+1)
        return dp[0]-1
        

    def isPal(self,s):
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def minCut_1(self,s):
        self.val=2**10
        self.dfs(s,0,0)
        return self.val
    def dfs(self,s,start,cut,):
        if start==len(s):
            if self.val>cut-1:
                self.val=cut-1
            return 
        for  i in range(len(s)-1,start-1,-1):
            if self.isPal(s[start:i+1]):
                self.dfs(s,i+1,cut+1)
        
                
if __name__=='__main__':
    sol=Solution()
    s='aaa'
    print sol.minCut_1(s)
