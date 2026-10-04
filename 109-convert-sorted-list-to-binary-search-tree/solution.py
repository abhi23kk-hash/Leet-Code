class Solution:
    def sortedListToBST(self, head):
        a = []

        while head:
            a.append(head.val)
            head = head.next

        def f(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            n = TreeNode(a[m])

            n.left = f(l, m - 1)
            n.right = f(m + 1, r)

            return n

        return f(0, len(a) - 1)