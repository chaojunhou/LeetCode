# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor1(self, root, p, q):
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right,p,q)
            else:
                break
        return root
            
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
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(10)]
    num.sort()
    num = [1,2,3,4]
    root=sol.sortedArrayToBST(num)
    print sol.lowestCommonAncestor(root,TreeNode(1),TreeNode(4)).val
        
        
