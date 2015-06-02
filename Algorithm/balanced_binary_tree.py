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
    def isBalanced(self, root):
        def maxDepth(root):
            if not root:
                return 0
            Left = maxDepth(root.left)
            if Left == -1:
                return -1
            Right = maxDepth(root.right)
            if Right == -1:
                return -1
            return  max(Left,Right)+1 if abs(Left-Right) < 2 else -1
        return maxDepth(root) != -1
if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(None)
    root= TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print tree.printTree(root)
    print sol.isBalanced(root)
