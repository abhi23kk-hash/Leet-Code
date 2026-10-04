class Solution:
    def restoreIpAddresses(self, s):
        ans = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    ans.append('.'.join(parts))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) <= 255:
                    backtrack(end, parts + [part])

        backtrack(0, [])
        return ans