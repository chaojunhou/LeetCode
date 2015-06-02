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
            dummy.next = heapq.heappop(heap)[1]
            dummy = dummy.next
            if dummy.next:
                heapq.heappush(heap,(dummy.next.val,dummy.next))
        return dummy.next
    def mergeKLists_1(self,lists):
        n=len(lists)
        if n==0 :
            return None
        if n == 1:
            return lists[0]
        mid = n/2
        return self.merge(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
    def merge(self,head1,head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
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
if __name__ == '__main__' :
    sol = Solution
    
