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
            self.printTree(root.left)
            print root.val
            self.printTree(root.right)
    def preorderTraversal(self,root):
        if not root:
            return []
        if root and not root.left and not root.right:
            return [root.val]
        else:           
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
    def iterative_preorder(self,root):
        res=[]
        stack=[]
        if root:
            stack.append(root)
            while stack:
                node=stack.pop()
                res.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
        return res
            
    def inorderTraversal(self,root):
        lst=[]
        if root:
            lst+=self.inorderTraversal(root.left)
            lst.append(root.val)
            lst+=self.inorderTraversal(root.right)
        return lst
    def iterative_inorder(self,root):
        res=[]
        stack=[]
        while root:
            stack.append(root)
            root=root.left
        while stack:
            node=stack.pop()
            res.append(node.val)
            x=node.right
            while x:
                stack.append(x)
                x=x.left
        return res
    def postorderTraversal(self,root):
        lst=[]
        if root:
            lst+=self.postorderTraversal(root.left)
            lst+=self.postorderTraversal(root.right)
            lst.append(root.val)
        return lst        
    def iterative_postorder(self,root):
        pre=None
        stack=[]
        lst=[]
        if root:
            stack.append(root)
            while stack:
                curr=stack[-1]
                if curr.left is None and curr.right is None ://if the root just pop
                    lst.append(curr.val)
                    stack.pop()
                    pre=curr
                elif pre and (pre==curr.left or pre==curr.right)://if just one branch
                    lst.append(curr.val)
                    stack.pop()
                    pre=curr
                else:
                    if curr.right:
                        stack.append(curr.right)// the right subtree first
                    if curr.left: 
                        stack.append(curr.left)  //the left subtree second
                    
        return lst
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(8)]
    num.sort()
    print num
    root=sol.sortedArrayToBST(num)
    print sol.preorderTraversal(root)
    print sol.iterative_preorder(root)
        
