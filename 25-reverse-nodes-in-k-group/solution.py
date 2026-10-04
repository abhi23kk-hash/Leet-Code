class Solution:
    def reverseKGroup(self, head, k):
        values = []

        while head:
            values.append(head.val)
            head = head.next

        for i in range(0, len(values), k):
            if i + k <= len(values):
                values[i:i + k] = values[i:i + k][::-1]

        dummy = ListNode(0)
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next