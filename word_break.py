class Solution:
    def wordBreak(self,s,dict):
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i]=True
        return dp[len(s)]
        

if __name__=='__main__':
    sol=Solution()
    s='leetcode'
    dict=['leet','code']
    print sol.wordBreak(s,dict)
