class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeElements(self, head, val):
        if not head:
            return None
        dummy = q = ListNode(-1)
        while head:
            if head.val == val:
                head = head.next
            else:
                q.next = head
                head = head.next
                q = q.next
        q.next = None
        return dummy.next
                


if __name__ == '__main__':
    sol = Solution()
    lst = [1,2,6,3,4,5]
    #lst = [1,1]
    head=p= ListNode(-1)
    for value in lst:
        p.next = ListNode(value)
        p = p.next
    p.next = None
    val = 6
    p = sol.removeElements(head.next, val)
    print 'fuck'
    while p :
        print p.val
        p = p.next
    print 'das'
    
