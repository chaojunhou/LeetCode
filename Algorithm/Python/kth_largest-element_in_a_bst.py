# Definition for a  binary tree node
class TreeNode:    
    def __init__(self, x):
                   
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.creatTree(num,0,len(num)-1)
    def creatTree(self,num,begin,end):
        if begin >end:
            return None
        mid=(begin+end)/2
        root=TreeNode(num[mid])
        root.left=self.creatTree(num,begin,mid-1)
        root.right=self.creatTree(num,mid+1,end)
        return root
    def printTree(self, root):
        if root:
            if root.left:
                self.printTree(root.left)
            print root.val
            if root.right:
                self.printTree(root.right)
    def KthSmallest1 (self, root, k):
        self.ans = []
        self.getTree(root)
        return self.ans[k-1]
    def KthSmallest(self, root, k):
        self.c = 0
        self.k = 0
        self.getK(root,k)
        return self.k
    def getK(self, root, k):
        if root:
            self.getK(root.left,k,)
            self.c += 1
            if self.c == k:
                self.k = root.val
                return 
            self.getK(root.right, k)
            
    def getTree(self, root):
        if root:
            if root.left:
                self.getTree(root.left)
            self.ans.append(root.val)
            if root.right:
                self.getTree(root.right)
            
if __name__ == '__main__':
    sol = Solution()
    import random
    num = [random.randint(1,100) for i in range(10)]
    num.sort()
    print num
    root = sol.sortedArrayToBST(num)
    print sol.KthSmallest(root,3)
    print sol.KthSmallest1(root,3)
