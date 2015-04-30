class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def mergeTwoLists(self,l1,l2):
        dummy=p= ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1 
        if l2:
            p.next = l2
        return dummy.next

if __name__=='__main__':
    head1=l1=ListNode(1)
    l1.next=ListNode(3)
    root = ListNode(-1)
    l1.next.next=None
    while l1!=None:
        l1 = l1.next 
    head2=l2=ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = None
    while l2 :
        l2 = l2.next
    sol=Solution()
    root= sol.mergeTwoLists(head1,head2)
    while root:
        print root.val
        root = root.next
    
