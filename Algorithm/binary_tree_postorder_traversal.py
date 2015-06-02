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
                if curr.left is None and curr.right is None :
                    lst.append(curr.val)
                    stack.pop()
                    pre=curr
                elif pre and (pre==curr.left or pre==curr.right):
                    lst.append(curr.val)
                    stack.pop()
                    pre=curr
                else:
                    if curr.right:
                        stack.append(curr.right)
                    if curr.left:
                        stack.append(curr.left)
                    
        return lst
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(3)]
    num.sort()
    print num
    root=sol.sortedArrayToBST(num)
    print sol.postorderTraversal(root)
    print sol.iterative_postorder(root)
        
