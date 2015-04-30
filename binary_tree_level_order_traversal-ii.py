class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrderBottom(self,root):
        res= [] 
        def dfs(root,depth):
            if root:
                if self.cur == depth:
                    res.append([root.val])
                    self.cur += 1
                else:
                    res[depth].append(root.val)
                dfs(root.left,depth+1)
                dfs(root.right,depth+1)
        if root:
            self.cur = 0
            dfs(root,0)
        return res[::-1]
            
            
        
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.levelOrderBottom(root)
