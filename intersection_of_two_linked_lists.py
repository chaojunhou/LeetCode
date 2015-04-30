class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy=ListNode(-1)
        p=dummy
        carry=0
        while l1 and l2:
            p.next=ListNode((l1.val+l2.val+carry)%10)
            carry=(l1.val+l2.val+carry)/10
            l1=l1.next
            l2=l2.next
            p=p.next
        while l1:
            p.next=ListNode((l1.val+carry)%10)
            carry=(l1.val+carry)/10
            p=p.next
            l1=l1.next
            
        while l2:
            p.next=ListNode((l2.val+carry)%10)
            carry=(l2.val+carry)/10
            p=p.next
            l2=l2.next
        if carry:
            p.next=ListNode(carry)
        return dummy.next
            

if __name__=='__main__':
    sol=Solution()
    head1=l1=ListNode(1)
    lst1=[2,4,3]
    for element in lst1:
        l1.next=ListNode(element)
        l1=l1.next
    l1.next=None
    head2=l2=ListNode(5)
    lst2=[6,4,7]
    for element in lst2:
        l2.next=ListNode(element)
        l2=l2.next
    l2.next=None
    head=sol.addTwoNumbers(head1,head2)
    print 'fuck'
    while head:
        print head.val
        head=head.next
