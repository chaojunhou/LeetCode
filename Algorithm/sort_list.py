class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        head1=head
        head2=slow.next
        slow.next=None
        return self.merge(self.sortList(head1), self.sortList(head2))
    def merge(self,head1,head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head2
        dummy=ListNode(-1)
        pre=dummy
        while head1 and head2:
            if head1.val<head2.val:
                pre.next=head1
                head1=head1.next
            else:
                pre.next=head2
                head2=head2.next
            pre=pre.next
        if head1 is None:
            pre.next = head2
        if head2 is None:
            pre.next = head1
        return dummy.next 
         
if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[2,4,3,5]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    List.next=None
    head1=sol.sortList(head)
    print 'fuck'
    while head1:
        print head1.val
        head1=head1.next
