class Solution:
    def nextLargerNodes(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        ans = [0] * len(arr)
        stack = []

        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] < val:
                ans[stack.pop()] = val
            stack.append(i)

        return ans