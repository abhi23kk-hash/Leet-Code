class Solution:
    def minimumTotal(self, t):
        a = t[-1][:]

        for i in range(len(t) - 2, -1, -1):
            for j in range(len(t[i])):
                a[j] = t[i][j] + min(a[j], a[j + 1])

        return a[0]