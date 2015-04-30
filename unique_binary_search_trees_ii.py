class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def numTrees(self,n):
        if n==0 or n==1:
            return 1     
        else:
            cunt=[0 for i in range(n+1)]
            cunt[0]=1
            cunt[1]=1
            for i in range(2,n+1):
                for j in range(0,i):
                    cunt[i]+=cunt[j]*cunt[i-1-j]
            return cunt[n]
    def printTree(self,root):
        if root:
            print root.val,
            self.printTree(root.left)
            self.printTree(root.right)
    def generateTrees(self,n):
        return self.dfs(1,n)
    def dfs(self,begin,end):
        if begin>end:
            return [None]
        res=[]
        for rootvalue in range(begin,end+1):
            LeftTree=self.dfs(begin,rootvalue-1)
            RightTree=self.dfs(rootvalue+1,end)
            for leftNode in LeftTree:
                for rightNode in RightTree:
                    root=TreeNode(rootvalue)
                    root.left=leftNode
                    root.right=rightNode
                    res.append(root)
        return res
            
        
if __name__=='__main__':
    sol=Solution()
    for x in sol.generateTrees(5):
        sol.printTree(x)
        print 
