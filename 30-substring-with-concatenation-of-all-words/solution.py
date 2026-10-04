class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        n = len(words[0])
        m = len(words)
        l = n * m

        d = {}

        for w in words:
            d[w] = d.get(w, 0) + 1

        ans = []

        for i in range(len(s) - l + 1):
            t = {}

            for j in range(i, i + l, n):
                w = s[j:j + n]

                if w not in d:
                    break

                t[w] = t.get(w, 0) + 1

                if t[w] > d[w]:
                    break

            else:
                ans.append(i)

        return ans