class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def reverseKGroup1(self,head,k):
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
    def reverseKGroup(self,head,k):
        pre=tail=dummy = ListNode(-1)
        dummy.next = head
        while 1:
            count = k
            while tail and count:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next # for the next cycle
            while pre.next != tail:
                p = pre.next # assign
                pre.next = p.next # delete
                p.next = tail.next # tail the beging of the reverse list
                tail.next = p  # insert
            tail = head
            pre = head
        return dummy.next
            
        
if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[2,3,4,5]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    List.next=None
    head1=sol.reverseKGroup(head,3)
    while head1:
        print head1.val
        head1=head1.next
