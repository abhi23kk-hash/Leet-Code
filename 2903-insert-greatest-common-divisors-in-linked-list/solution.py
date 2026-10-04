class Solution:
    def insertGreatestCommonDivisors(self, head):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head

        while curr and curr.next:
            node = ListNode(gcd(curr.val, curr.next.val))
            node.next = curr.next
            curr.next = node
            curr = node.next

        return head