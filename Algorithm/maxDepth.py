import random
class BNode:
    left,right,data=None,None,0
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
class TreeNode:
    def __init__(self):
        self.root=None
        
    def Insert(self,root,node):
        if root is None:
            
            return self.addNode(node)
        else:
            if root.val>=node:
                root.left=self.Insert(root.left,node)
                
               
            if root.val<node:
                root.right=self.Insert(root.right,node)
        return root
    def addNode(self,data):
        return BNode(data)
        

    def maxDepth(self,root):
        
        if root==None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        
    
if __name__=='__main__':
    BinTree=TreeNode()
    root=BinTree.addNode(0)
    for i in range(50):
        BinTree.Insert(root,random.randint(1,50))
    print BinTree.maxDepth(root)

    
    
    
