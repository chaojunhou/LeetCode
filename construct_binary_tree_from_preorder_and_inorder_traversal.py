class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
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
            print root.val
            self.printTree(root.left)
            
            self.printTree(root.right)
            
    def buildTree(self,preorder,inorder):
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root

    
    def buildTree_1(self,inorder,postorder):
        if len(postorder)==0:
            return None
        root=TreeNode(postorder[-1])
        index=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:index],postorder[:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        return root
    
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(4)]
    num.sort()
    root=sol.buildTree([1,2,3],[2,1,3])
    sol.printTree(root)
    root=sol.buildTree_1([2,1,3],[2,3,1])
    sol.printTree(root)

   
        
