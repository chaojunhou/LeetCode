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
if __name__ == '__main__':
    sol = Solution()
    import random
    num = [random.randint(1,100) for i in range(10)]
    num.sort()
    print num
    root = sol.sortedArrayToBST(num)
    sol.printTree(root)
