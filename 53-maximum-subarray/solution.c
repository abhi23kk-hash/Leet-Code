int maxSubArray(int* a, int n) {

    int s = a[0];
    int m = a[0];

    for (int i = 1; i < n; i++) {

        if (s < 0)
            s = a[i];
        else
            s += a[i];

        if (s > m)
            m = s;
    }

    return m;
}