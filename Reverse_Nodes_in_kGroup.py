class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def reverseKGroup(self,head):
        if not head or not head.next:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        start=dummy
        while start.next:
            end = start
            for i in range(k-1):
                end=end.next
                if end.next is None:
                    return dummy.next
            res=self.reverse(start.next,end.next)
            start.next=res[0]
            start=res[1]
        return dummy.next
    def reverse(self,begin,end):
        dummy=ListNode(-1)
        dummy.next=head
        while dummy.next!=end:
            tmp=begin.next
            begin.next=tmp.next
            tmp.next=dummy.next
            dummy.next=tmp
        return [end,begin]          
            
        
if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[2,3,4,5]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    List.next=None
    head1=sol.reverse(head)
    print 'fuck'
    while head1:
        print head1.val
        head1=head1.next
