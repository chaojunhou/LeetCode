class Solution:
    def subsets_1(self,S):
        res=[[]]
        length=len(S)
        for element in S:
            
            for index in range(0,length):
                temp=res[index]+[element]
                temp.sort()
                if temp not in res:
                    res.append(temp)
        return res
    def subsets(self,S):
        self.ans=[]
        S.sort()
        self.dfs(0,0,[])
        return self.ans
    

    def dfs(self,depth,start,Temp):
        if Temp not in self.ans:
            self.ans.append(Temp)
        length=len(S)
        if depth==length:
            return 
        for index in range(start,length):
            self.dfs(depth+1,index+1,Temp+[S[index]])


if __name__=='__main__':
    sol=Solution()
    S=[1,2,2]
    print sol.subsets_1(S)
