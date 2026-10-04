class Solution:
    def sortedArrayToBST(self, nums):
        def f(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            n = TreeNode(nums[m])

            n.left = f(l, m - 1)
            n.right = f(m + 1, r)

            return n

        return f(0, len(nums) - 1)