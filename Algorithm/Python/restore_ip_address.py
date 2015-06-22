class Solution:
    def restoreIPAddresses(self,s):
        self.res=[]      
        def dfs(s,part,ip):
            if part==4:
                if s=='':
                    self.res.append(ip[1:])
                return
            for i in range(1,4):
                if i<=len(s):
                    if int(s[:i])<=255:
                        dfs(s[i:],part+1,ip+'.'+s[:i])
                    if s[0]=='0':
                        break
        dfs(s,0,'')
        return self.res

if __name__=='__main__':
    sol=Solution()
    s="25525511135"
    print sol.restoreIPAddresses(s)
