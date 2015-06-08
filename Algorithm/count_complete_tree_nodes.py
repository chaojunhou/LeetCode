class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self,num):
        return self.creatTree(num,0,len(num)-1)
    def creatTree(self,num,begin,end):
        if begin >end:
            return None
        mid=(begin+end)/2
        root=TreeNode(num[mid])
        root.left=self.creatTree(num,begin,mid-1)
        root.right=self.creatTree(num,mid+1,end)
        return root
    def printTree(self,root):
        if root:
            self.printTree(root.left)
            print root.val
            self.printTree(root.right)
    def countNodes(self, root):
        if not root:
            return 0
        L = root
        R = root
        hleft = 0
        hright = 0
        while L:
            hleft += 1
            L = L.left
        while R:
            hright += 1
            R = R.right
        if hleft == hright:
            return 2**hleft -1
        return  self.GetNodeNumKthLevel(root, hright) + 2**(hright-1) - 1
    def GetNodeNumKthLevel(self, root, k):
        if k == 0 or root is None:
            return 0
        if k ==1:
            return 1
        return self.GetNodeNumKthLevel(root.left, k-1) + self.GetNodeNumKthLevel(root.right, k-1)
    def countNodes1(self, root):
        def height(root):
            if not root:
                return -1
            return 1 + height(root.left)
        h = height(root)
        if h < 0:
            return 0
        if height(root.right) == h-1:
            return 2**h + self.countNodes1(root.right)
        else:
            return 2**h + self.countNodes1(root.left)

if __name__ == '__main__':
    sol = Solution()
    import random
    num=[x for x in range(7)]
    num.sort()
    print num
    
    root = sol.sortedArrayToBST(num)
    print len(num), sol.countNodes1(root)
