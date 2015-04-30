class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    res=[]
    def printTree(self, root):
        if not root:
            return []
        if root:
            self.res.append(root.val)
            if root.left:
                self.printTree(root.left)
            if root.right:
                self.printTree(root.right)
        return self.res

class Solution:
    def rightSideView(self, root):
        
        def dfs(root,depth):
            if root:
                if self.cur < depth:
                    self.cur = depth
                    res.append(root.val)

                dfs(root.right,depth+1)
                dfs(root.left,depth+1)
        res = []
        if root:
            self.cur = -1
            dfs(root,0)
        return res
if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(None)
    root= TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    #root.right.right = TreeNode(5)
    print sol.rightSideView(root)
    


