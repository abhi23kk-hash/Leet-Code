class Solution:
    def doubleIt(self, head):
        def solve(node):
            if not node:
                return 0

            carry = solve(node.next)
            value = node.val * 2 + carry
            node.val = value % 10

            return value // 10

        carry = solve(head)

        if carry:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node

        return head