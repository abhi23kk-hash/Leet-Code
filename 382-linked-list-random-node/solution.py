import random

class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        curr = self.head
        result = curr.val
        i = 1

        while curr:
            if random.randrange(i) == 0:
                result = curr.val
            curr = curr.next
            i += 1

        return result