# Definition for a  binary tree node
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
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxSum=-2**10
        self.find(root)
        return self.maxSum
    def find(self,root):
        if not root:
            return 0
        left=max(self.find(root.left),0)
        right=max(self.find(root.right),0)
        self.maxSum=max(self.maxSum,root.val+left+right)
        return root.val+max(left,right)
    def maxPathSum1(self, root):

        self.maxSum = -2147483648
        find(root)
        return self.maxSum
    def find(self,root):
        if not root:
            return 0
        Left = self.find(root.left)
        Right = self.find(root.right)
        self.maxSum = max(root.val + Left + Right, self.maxSum)
        ret = root.val + max(Left,Right)
        return ret if ret > 0 else 0
        
if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(None)
    root= TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print tree.printTree(root)
    print sol.maxPathSum1(root)
