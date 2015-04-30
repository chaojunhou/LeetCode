class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def connect(self,root):
        if root:
            p=root
            q=None
            nextNode=None
            while p:
                if p.left:
                    if q:
                        q.next=p.left
                    q=p.left
                    if nextNode==None:
                        nextNode=q
                if p.right:
                    if q:
                        q.next=p.right
                        q=p.right
                        if nextNode==None:
                            nextNode=q
                p=p.next
            self.connect(nextNode)
        def connect_1(self,root):
            curr=root
            while curr:
                firstNodeInNextLevel=None
                prev=None
                while curr:
                    if not firstNodeInNextLevel:
                        if curr.left:
                            fistNodeInNextLevel=curr.left
                        else:
                            firstNodeInNextLevel=curr.right
                    if curr.left:
                        if prev:
                            prev.next=curr.left
                        prev=curr.left
                    if curr.right:
                        if prev:
                            prev.next=curr.right
                        prev=curr.right
                    curr=curr.next
                curr=firstNodeInNextLevl
        def connect_2(self,root):
            if root:
                if root.left and root.right:
                    root.left.next=root.right
                    tmp=root.next
                    while tmp:
                        if tmp.left:
                            root.right.next=tmp.left
                            break
                        if tmp.right:
                            root.right.next=tmp.right
                            break
                        tmp=tmp.next
                elif root.left:
                    tmp=root.next
                    while tmp:
                        if tmp.left:
                            root.left.next=tmp.left
                            break
                        if tmp.right:
                            root.left.next=tmp.right
                            break
                        tmp=tmp.next
                elif root.right:
                    tmp=root.next
                    while tmp:
                        if tmp.left:
                            root.right.next=tmp.left
                            break
                        if tmp.right:
                            root.right.next=tmp.right
                            break
                        tmp=tmp.next
                self.connect(root.right)
                self.connect(root.left)
                        
                
                    
            
                
if __name__=='__main__':
    
    sol=Solution()
    
    head=l1=ListNode(1)
    lst1=[1,2,3,3,3,4,4,5,5,6,7,7]
    for element in lst1:
        l1.next=ListNode(element)
        l1=l1.next
        
    l1.next=None
    head1=head
    while head1:
        print head1.val,
        head1=head1.next
    list_head=sol.deleteDuplicates(head)
    print 
    while list_head:
        print list_head.val,
        list_head=list_head.next
