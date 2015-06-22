class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def insertionSortList(self,head):
        if not head:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        cur=head
        while cur.next:
            if cur.val>cur.next.val:
                pre=dummy
                while pre.next.val<cur.next.val:
                    pre=pre.next
                tmp=cur.next
                cur.next=tmp.next
                tmp.next=pre.next
                pre.next=tmp
            else:
                cur=cur.next
        return dummy.next
if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[4,3,5,2]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    head1=sol.insertionSortList(head)
    #head1=sol.fuck(head)
    print 'fuck'
    while head1:
        print head1.val
        head1=head1.next
