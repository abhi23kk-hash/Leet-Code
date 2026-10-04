class Solution:
    def numComponents(self, head, nums):
        s = set(nums)
        count = 0

        while head:
            if head.val in s and (head.next is None or head.next.val not in s):
                count += 1
            head = head.next

        return count