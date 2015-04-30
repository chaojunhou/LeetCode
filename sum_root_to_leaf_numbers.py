class treeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None
class Solution:
    def sumNumbers(self,root):
        self.summ=0
        ans=0
        self.dfs(root,ans,self.summ)
        return self.summ
    def dfs(self,root,ans,summ):
        if not root:
            self.summ+=ans
            ans=0
            return 
        if root:
            if not root.left and not root.right:
                self.summ+=ans+root.val
                ans=0
                return
        if root.left:
            self.dfs(root.left,10*(ans+root.val),summ)
        if root.right:
            self.dfs(root.right,10*(ans+root.val),summ)
        
        
    def preorder(self,root):
        if root:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)
   
if __name__=='__main__':
    root=tree=treeNode(9)
   #tree.left=treeNode(9)
    #tree.left.right=treeNode(1)
    #tree.left.left=treeNode(11)
    #tree.left.left.left=treeNode(7)
    #tree.left.left.right=treeNode(2)
    #tree.right=treeNode(0)
    #tree.right.left=treeNode(13)
    #tree.right.right=treeNode(4)
    #tree.right.right.right=treeNode(1)    
    sol=Solution()
    print sol.sumNumbers(root)












