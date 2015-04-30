from random import choice
class RandomListNode:
    def __init__(self,x):
        self.label=x
        self.next=None
        self.random=None
class Solution:
    def copyRandomList(self,head):
        if not head:
            return None
        newHead=RandomListNode(head.label)
        dic={}
        #dic[head]=newHead
        pre=newHead
        node= head.next
        while node:
            newNode=RandomListNode(node.label)
            dic[node]=newNode
            pre.next=newNode
            pre=newNode
            node=node.next
        node=head
        copyNode=newHead
        while node:
            copyNode.random=dic[node.random]
            copyNode=copyNode.next
            node=node.next
        return newHead
    def copyRandomList1(self,head):
        if not head:
            return None
        dummy = RandomListNode(0)
        dic={None:None}
        p = head
        q = dummy
        while p:
            q.next = RandomListNode(p.label)
            dic[p] = q.next
            p = p.next
            q = q.next
        p = head
        q = dummy
        while p:
            print p.random.label
            q.next.random = dic[p.random]
            p = p.next
            q = q.next
        return dummy.next
if __name__=='__main__':
    sol=Solution()
    List=head=RandomListNode(1)
    lst=[2,3,4,5]
    for x in lst:
        List.next=RandomListNode(x)
        List=List.next
    List.next=None
    List = head
    
    while List:
        List.random = 
    head1=sol.copyRandomList1(head)
    print 'fuck'
    while head1:
        print head1.label
        head1=head1.next
