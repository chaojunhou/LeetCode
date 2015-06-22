class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:

    def getIntersectionNode(self, headA, headB):
        
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        tmp = 0
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if not p1:
                p1= headB
                tmp += 1
                if tmp == 2:
                    return None  
            if not p2 :
                p2 = headA
        return p1
                
    def getIntersectionNode1(self, headA, headB):
        p=headA
        q=headB
        lenA=self.length(p)
        lenB=self.length(q)
        if lenA==0 or lenB==0:
            return None
        if lenA>lenB:
            diff=lenA-lenB
            go=0
            while go<diff:
                headA=headA.next
                go+=1
            while headA!=headB:
                headA=headA.next
                headB=headB.next
            return headA
        else:
            diff=lenB-lenA
            go=0
            while go<diff:
                headB=headB.next
                go+=1
            while headA!=headB:
                headA=headA.next
                headB=headB.next
            return headB
    def length(self,head):
        count=0
        while head:
            count+=1
            head=head.next
        return count                

if __name__=='__main__':
    sol=Solution()
    p=head1=l1=ListNode(1)
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
    l2.next = p.next.next
    #l2.next = None
    print p.next.next.val
    print sol.getIntersectionNode(head1,head2).val

