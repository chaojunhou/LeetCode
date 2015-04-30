class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def partition(self,head,x):
        dummy1=ListNode(-1)
        dummy2=ListNode(-1)
        phead1=dummy1
        phead2=dummy2

        while head:
            if head.val<x:
                phead1.next=head
                phead1=phead1.next
            else:
                phead2.next=head
                phead2=phead2.next
            head=head.next
        phead2.next=None
        phead1.next=dummy2.next
        return dummy1.next
        
                

        
        


if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[4,3,2,5,2]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    head1=sol.partition(head,3)
    print 'fcuk'
    while head1:
        print head1.val
        head1=head1.next
