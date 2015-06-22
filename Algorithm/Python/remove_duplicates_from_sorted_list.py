class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteDuplicates(self,head):     
        if head is None:
            return head
        pre=dummy=ListNode(1)
        pre.next=head
        current=head
        while(pre.next):
            while current.next and current.next.val==pre.next.val:
                current=current.next      
            else:
                if pre.next==current:
                    pre=pre.next
                    current=pre.next
                else:
                    pre.next=current.next
        return dummy.next
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
