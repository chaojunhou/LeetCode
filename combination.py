class Solution:
    def find(self,n,k,Temp):
        if k==0:
            self.ans.append(Temp[::-1])
        else:
            i=k
            while i<=n:
                Temp.append(i)
                self.find(i-1,k-1,Temp)
                Temp.pop()#restore 
                i+=1
    def combine_1(self,n,k):
        self.ans=[]
        Temp=[]
        self.find(n,k,Temp)
        return self.ans
           
    def combine(self,n,k):
        self.res=[]
        tmp=[]
        self.dfs(n,k,1,0,tmp)
        return self.res
    def dfs(self,n,k,m,p,tmp):
        if k==p:
            self.res.append(tmp[:])
            return
        for i in range(m,n+1):
            tmp.append(i)
            print tmp,
            print '-before'
            self.dfs(n,k,i+1,p+1,tmp)
            print tmp,
            print '---after'
            tmp.pop()
    def subset(self,S):
        ans=[]
        n=len(S)
        S.sort()
        for index in range(1<<n):
            ans.append(self.print_subset(S,n,index))
        return ans
    def print_subset(self,S,n,s):
        res=[]
        for index in range(n):
            if s&(1<<index):
                
                res.append(S[index])
        return res


if __name__=='__main__':
    sol=Solution()
    from pprint import pprint
    S=[4,1,0]
    #pprint(sol.subset(S))
    print sol.combine(4,3)
