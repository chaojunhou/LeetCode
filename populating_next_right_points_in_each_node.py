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
    def connet(self,root):
        if root and root.left:
            if root.left and root.right:  
                root.left.next=root.right
            if root.next:
                root.right.next=root.next.left
            else:
                root.right.next=None
        self.connet(root.left)
        self.connet(root.right)
if __name__=='__main__':
    root=tree=treeNode(1)
    tree.left=treeNode(2)
    tree.left.left=treeNode(4)
    tree.left.right=treeNode(5)
    tree.right=treeNode(3)
    tree.right.left=treeNode(6)
    tree.right.right=treeNode(7)
    tree.preorder(root)
