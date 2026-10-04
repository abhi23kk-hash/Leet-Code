class Solution:
    def flatten(self, head):
        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                next_node = curr.next
                child = self.flatten(curr.child)

                curr.next = child
                child.prev = curr
                curr.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                tail.next = next_node

                if next_node:
                    next_node.prev = tail

            curr = curr.next

        return head