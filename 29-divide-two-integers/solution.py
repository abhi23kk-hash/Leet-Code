class Solution:
    def divide(self, a, b):
        if a == -2147483648 and b == -1:
            return 2147483647

        s = 1
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            s = -1

        a = abs(a)
        b = abs(b)

        c = 0

        while a >= b:
            t = b
            d = 1

            while a >= (t << 1):
                t <<= 1
                d <<= 1

            a -= t
            c += d

        if s == -1:
            return -c
        return c