class Solution:
    def pairSum(self, head):
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        ans = 0
        left = head
        right = prev

        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans