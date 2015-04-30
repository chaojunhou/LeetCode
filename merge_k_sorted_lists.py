class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def mergeKLists(self,lists):
        import heapq
        heap=[]
        dummy=ListNode(-1)
        for node in lists:
            if node:
                heap.append((node.val,node))
        heapq.heapify(heap)
        while heap:
            tmp=heapq.heappop(heap)
            dummy.next=ListNode(tmp[0])
            if tmp[1]:
                heapq.heappush(heap,(tmp[1].next.val,tmp[1].next))
        return dummy.next
    def mergeKLists_1(self,lists):
        n=len(lists)
        if n==0 or lists is None:
            return None
        while n>1:
            k=(n+1)/2
            for i in range(n/2):
                self.merge(lists[i],lists[i+k])
            n=k
        return lists[0]
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
            pre.next=head2
        if head2 is None:
            pre.next=head1
        return dummy.next  
