class Solution:
    def removeNodes(self, head):
        stack = []

        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next

        dummy = ListNode(0)
        curr = dummy

        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next