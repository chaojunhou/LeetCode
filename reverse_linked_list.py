class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseList1(self, head):

        if  (not head) or (not head.next):
            return head
        q = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return q
    def reverseList2(self, head):
        pre = None
        cur = head
        while cur:
            p = cur.next # 把当前的指针链接到前一个元素
            cur.next = pre
            pre = cur
            cur = p
        return pre
    def reverseList3(self, head):
        
        def reverse(head,newHead):
            if not head:
                return newHead
            cur = head.next
            head.next = newHead
            return reverse(cur,head)
            
        return reverse(head,None)
        
    def reverseList(self, head):
        dummy = ListNode(-1)
        cur = None
        dummy.next = cur
        while head :
            q = head.next # 防止断链
            dummy.next = head
            head.next = cur
            cur = head
            head = q
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
    p = sol.reverseList2(head.next)
    print 'fuck'
    while p :
        print p.val
        p = p.next
    print 'das'
