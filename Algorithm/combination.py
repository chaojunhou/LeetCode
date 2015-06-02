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
    def combine_2(self, n, k):
        self.res = []
        self.helper(n, k, 0, 1, [])
        return self.res
    def helper(self, n, k, depth, val, ans):
        if depth == k:
            self.res.append(ans[:])
            return 
        for i in range(val, n+1):
            self.helper(n, k, depth+1, i+1, ans + [i])
        
           
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



if __name__=='__main__':
    sol=Solution()
    from pprint import pprint
    S=[4,1,0]
    print sol.combine_2(1, 1)
    print sol.combine_2(4, 3)
