class Solution:
   
    def isValidBST(self,root):
        if not root:
            return True
        self.pre=None
        return self.check(root)
    def check(self,root):
        if root:
            if not self.check(root.left):
                return False
            if self.pre and self.pre.val>=root.val:
                return False
            self.pre=root
            self.check(root.right)
        return True
