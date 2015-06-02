class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def insertionSortList(self,head,k):
        if not head :
            return head
        p=head
        count=1
        dummy=ListNode(-1)
        while p.next:
            count+=1
            p=p.next
        step=count-k%count
        q=head
        count=1
        while count<step:
            count+=1
            q=q.next
        p.next=head
        dummy.next=q.next
        q.next=None
        return dummy.next
                
if __name__=='__main__':
    sol=Solution()
    List=head=ListNode(1)
    lst=[2,3,4,5]
    for x in lst:
        List.next=ListNode(x)
        List=List.next
    List.next=None
    head1=sol.insertionSortList(head,2)
    #head1=sol.fuck(head)
    print 'fuck'
    while head1:
        print head1.val
        head1=head1.next
