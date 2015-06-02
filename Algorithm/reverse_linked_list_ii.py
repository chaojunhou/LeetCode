class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        pre=dummy = ListNode(-1)
        dummy.next = head
        count = 1
        while count < m:
            pre = pre.next
            head = head.next
            count += 1
        while count < n:
            p = head.next
            head.next = p.next
            p.next = pre.next
            pre.next = p
            count += 1
        return dummy.next
        
              


if __name__ == '__main__':
    sol = Solution()
    lst = [1,2,6,3,5,4]#
    #lst = [1,2]
    head=p= ListNode(-1)
    for value in lst:
        p.next = ListNode(value)
        p = p.next
    p.next = None
    p = sol.reverseBetween(head.next,2,4)
    print 'fuck'
    while p :
        print p.val
        p = p.next
    print 'das'
