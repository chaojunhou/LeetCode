class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def zigzagLevelOrder(self,root):
        res= []
        self.cur = 0
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
            dfs(root,0)
        for i in range(self.cur):
            if i%2 ==1:
                res[i] = res[i][::-1]
        return res 
               
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.zigzagLevelOrder(root)
