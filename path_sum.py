class treeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None
    def preorder(self,root):
        if root:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)
class Solution:
    def hasPathSum(self,root,sum):
        if root:
            if not root.left and not root.right:
                if root.val==sum:
                    return True
            return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
        return False 
    def preorder(self,root):
        if root:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)
   
if __name__=='__main__':
    root=tree=treeNode(5)
    tree.left=treeNode(4)
    tree.left.left=treeNode(11)
    tree.left.left.left=treeNode(7)
    tree.left.left.right=treeNode(2)
    tree.right=treeNode(8)
    tree.right.left=treeNode(13)
    tree.right.right=treeNode(4)
    tree.right.right.right=treeNode(1)
    root=None
    
    sol=Solution()
    print sol.hasPathSum(root,22)
    
