int* spiralOrder(int** a, int n, int* c, int* rs) {

    int* b = (int*)malloc(n * (*c) * sizeof(int));

    int t = 0;
    int d = n - 1;
    int l = 0;
    int r = *c - 1;

    int k = 0;

    while (t <= d && l <= r) {

        for (int i = l; i <= r; i++)
            b[k++] = a[t][i];

        t++;

        for (int i = t; i <= d; i++)
            b[k++] = a[i][r];

        r--;

        if (t <= d) {

            for (int i = r; i >= l; i--)
                b[k++] = a[d][i];

            d--;
        }

        if (l <= r) {

            for (int i = d; i >= t; i--)
                b[k++] = a[i][l];

            l++;
        }
    }

    *rs = k;

    return b;
}