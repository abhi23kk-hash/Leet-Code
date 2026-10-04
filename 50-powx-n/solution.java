class Solution {
    public double myPow(double x, int n) {

        long a = n;

        if (a < 0) {
            x = 1 / x;
            a = -a;
        }

        double r = 1;

        while (a > 0) {

            if ((a & 1) == 1)
                r *= x;

            x *= x;
            a >>= 1;
        }

        return r;
    }
}