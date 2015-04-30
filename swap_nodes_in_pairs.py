class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def swapPairs(self,head):
        pre=dummy=ListNode(-1)
        dummy.next=head
        cur=head
        last=cur.next
        while cur and last:
            cur.next=last.next
            last.next=cur
            pre.next=last
            pre=pre.next.next
            if cur.next:
                cur=cur.next
            else:
                break
            last=cur.next
        return dummy.next
        

if __name__=='__main__':
    sol=Solution()
    head=l1=ListNode(None)
    lst1=[]
    for element in lst1:
        l1.next=ListNode(element)
        l1=l1.next
    l1.next=None
    List=sol.swapPairs(head)

    while List:
        print List.val,
        List=List.next
