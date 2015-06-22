class TreeNode:
     def __init__(self, x):
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
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
        
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(4)]
    num.sort()
    num = [38,57,67,82]
    print num
    root=sol.sortedArrayToBST(num)
    sol.printTree(root)
    print '-----'*4
    sol.printTree(sol.invertTree(root))
  
