class Solution:
    def subsets(self,S):
        res=[[]]
        length=len(S)
        for element in S:
            for index in range(0,length):
                temp=res[index]+[element]
               
                if temp not in res:
                    res.append(temp)
        return res
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
    S=[1,2,2]
    print sol.subsets(S)
