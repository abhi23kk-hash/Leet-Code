class Solution:
    def splitListToParts(self, head, k):
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        size = n // k
        extra = n % k
        result = []

        curr = head

        for i in range(k):
            part = curr
            length = size + (1 if i < extra else 0)

            for _ in range(length - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part)

        return result