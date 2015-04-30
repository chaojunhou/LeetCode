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
    def levelOrder(self,root):
        lst=[]
        if root:
            temp=[root]
            while len(temp)!=0:
                lst.append(temp)
                temp=[]
                for father in lst[-1]:
           
                    if father.left:
                        temp.append(father.left)
                    if father.right:
                        temp.append(father.right)
        lst=[[node.val for node in layer] for layer in lst]         
        return lst
    def levelOrder_1(self,root):
        lst=[]
        from collections import deque
        queue=[]
        cur=0
        last=1
        if root:
            queue.append(root)
            while cur<len(queue):
                last=len(queue)
                while cur<last:
                    lst.append(queue[cur].val)
                    if queue[cur].left:
                        queue.append(queue[cur].left)
                    if queue[cur].right:
                        queue.append(queue[cur].right)
                    cur+=1
        else:
            return []
        ans=[]
        ans.append([lst[0]])
        x=1
        while x<len(lst):           
            if 2*x+1>len(lst):
                break
            else:
                ans.append(lst[x:2*x+1])
                x=2*x+1  
        if x!=len(lst):
            ans.append(lst[x:])  
        return ans
    def levelOrder_2(self,root):
        lst=[]
        from collections import deque
        queue=deque([])
        if root:
            queue.append(root)
            while queue:
                curr=queue[0]
                if curr:
                    lst.append(curr.val)
                    queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return lst
    def levelOrderBottom(self,root):
        self.ans=[]
        self.dfs(root,0)
        self.ans=self.ans[::-1]
        return self.ans
    def dfs(self,root,depth):
        if  root:
            if depth=
            =len(self.ans):
                self.ans.append([root.val])
            else:
                self.ans[depth].append(root.val)
            self.dfs(root.left,depth+1)
            self.dfs(root.right,depth+1)
        
        
if __name__=='__main__':
    sol=Solution()
    import random
    num=[random.randint(1,100) for x in range(4)]
    num.sort()
    print num
    root=sol.sortedArrayToBST(num)
    print sol.levelOrder(root)
    #print sol.levelOrder_1(root)#not worked when there is null in the subtree
    #print sol.levelOrder_2(root)
    print sol.levelOrderBottom(root)
        
