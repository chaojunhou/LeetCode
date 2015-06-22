class Solution:
    def sortedListToBST(self,head):
        n=0
        p=head
        while p:
            p=p.next
            n+=1
        self.dummy=head
        return sortList2BST(0,n-1)
    def sortList2BST(self,start,end):
        if start>end:
            return None
        mid=(start+end)/2
        leftchild=self.sortList2BST(start,mid-1)
        parent=TreeNode(self.dummy.val)
        parent.left=leftchild
        self.dummy=self.dummy.next
        parent.right=self.sortList2BST(mid+1,end)
        return parent
        
