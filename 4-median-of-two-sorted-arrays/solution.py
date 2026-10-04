class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)
        # ensure A is the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i

            # i is too small, must move right
            if i < m and j > 0 and B[j-1] > A[i]:
                imin = i + 1
            # i is too big, must move left
            elif i > 0 and j < n and A[i-1] > B[j]:
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])

                # odd total length -> median is max_left
                if (m + n) % 2 == 1:
                    return float(max_left)

                # even total length -> need min_right as well
                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])

                return (max_left + min_right) / 2.0
