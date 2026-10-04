class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            # Check odd length palindrome (centered at i)
            len1 = self.expand_from_center(s, i, i)
            # Check even length palindrome (centered between i and i+1)
            len2 = self.expand_from_center(s, i, i + 1)
            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_from_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
