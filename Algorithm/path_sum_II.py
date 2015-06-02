class treeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None
class Solution:
    def pathSum(self, root, sum):
        self.res=[]
        self.dfs(root,[],sum)
        return self.res
    def dfs(self,root,ans,sum):
        if root:
            if not root.left and not root.right:
                if root.val==sum:
                    self.res.append(ans+[root.val])
                else:
                    return 
            if root.left:
                self.dfs(root.left,ans+[root.val],sum-root.val)
            if root.right:
                self.dfs(root.right,ans+[root.val],sum-root.val)  
   
if __name__=='__main__':
    root=tree=treeNode(5)
    tree.left=treeNode(4)
    tree.left.left=treeNode(11)
    tree.left.left.left=treeNode(7)
    tree.left.left.right=treeNode(2)
    tree.right=treeNode(8)
    tree.right.left=treeNode(13)
    tree.right.right=treeNode(4)
    tree.right.right.left=treeNode(5)
    tree.right.right.right=treeNode(1)
    
    sol=Solution()
    print sol.pathSum(root,22)
    
