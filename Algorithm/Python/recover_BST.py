class Solution:
    def recoverTree(self,root):
        if not root:
            return
        self.r1,self.r2=None,None
        self.pre=None
        self.find(root)
        self.r1.val,self.r2.val=self.r2.val,self.r1.val
        return root
    def find(self,root):
        if root:
            self.find(root.left)
            if self.pre and self.pre.val>root.val:
                self.r2=root
                if self.r1 is None:
                    self.r1=self.pre
            self.pre=root
            self.find(root.right)
