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
     def lowestCommonAncestor(self, root, p, q):
         
         
          self.pathLeft = []
          self.pathRight = []
          self.getNode(root,p,self.pathLeft)
          self.getNode(root,q,self.pathRight)
          res = None
          for left,right in zip(self.pathLeft,self.pathRight):
               print left.val,right.val
               if left.val == right.val:
                    res = left
          return res
                   
     def getNode(self, root, node, path):
          if not root:
               return False
          path.append(root)
          if root == node:
               return True
          found = self.getNode(root.left,node, path)
          if not found:
               found = self.getNode(root.right,node,path)
          if not found:
               path.pop()
          return found
          
               
               
                       
          

     def lowestCommonAncestor1(self, root, p, q):
          while root:
               if root.val > p.val and root.val > q.val:
                    return self.lowestCommonAncestor1(root.left,p,q)
               elif root.val < p.val and root.val < q.val:
                    return self.lowestCommonAncestor1(root.right,p,q)
               else:
                    break
          return root
    
     def lowestCommonAncestor2(self, root, p, q):
          if root:
               if self.find(root.left,p):
                    if self.find(root.right,q):
                         return root
                    else:
                         return self.lowestCommonAncestor2(root.left,p,q)
               else:
                    if self.find(root.left,q):
                         return root
                    else:
                         return self.lowestCommonAncestor2(root.right,p,q)
     def find(self, root, p):
          if not root or not p:
               return False
          if root.val == p.val:
               return True
          return self.find(root.left,p) or self.find(root.right,p)
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
    print sol.lowestCommonAncestor1(root,TreeNode(1),TreeNode(4)).val
        
        
