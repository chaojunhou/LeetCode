class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        right = len(lst)-1
        left = 0
        while left < right:
            if lst[left] == lst[right]:
                left += 1
                right -= 1
            else:
                return False
        return True 



if __name__ == '__main__':
    sol = Solution()
    import random
    lst = [random.randint(1,100) for i in range(5)]
    print lst
    p = head = ListNode(-1)
    for i in lst:
        p.next = ListNode(i)
        p = p.next
    p.next = None
    print sol.isPalindrome(head.next)
