class treeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None
class Solution:
    def flatten(self,root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.rgiht)
        p=root
        if p.left is None:
            return
        p=p.left
        while p.right:
            p=p.right
        p.right=root.right
        root.right=root.left
        root.left=None
    def flatten_1(self,root):
        p=root
        stack=[]
        while p or stack:
            
            if p.right:
                stack.append(p.right)
            if p.left:
                p.right=p.left
                p.left=None
            else:
                if stack:
                    temp=stack.pop()
                    p.right=temp
            p=p.right
    def preorder(self,root):
        stack=[]
        lst=[]
        while root or stack:
            if root :
                lst.append(root)
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return stack
    def inorder(self,root):
        stack=[]
        lst=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                lst.append(root)
                root=root.right
        return lst
    def postorder(self,root):
        stack=[]
        queue=[]
        queue.append(root)
        while queue:
            root=queue.pop()
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
            stack.append(root)
        return stack[::-1]
    def levelorder(self,root):
        from collections import deque
        if root:
            queue=deque([])
            while queue:
                root=q.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
    
    

    def preorder_1(self,root):
        if root:
            print root.val
            self.preorder(root.left)
            self.preorder(root.right)
   
if __name__=='__main__':
    root=tree=treeNode(0)
    tree.left=treeNode(10)
    tree.left.right=treeNode(1)
    tree.left.left=treeNode(11)
    tree.left.left.left=treeNode(7)
    tree.left.left.right=treeNode(2)
    tree.right=treeNode(0)
    tree.right.left=treeNode(13)
    tree.right.right=treeNode(4)
    tree.right.right.right=treeNode(1)    
    sol=Solution()
    sol.preorder_1(root)
    print sol.preorder(root)

