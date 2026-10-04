/**
 * Note: The returned array must be malloced.
 */

int** generateMatrix(int n, int* rs, int** cs) {

    int** a = (int**)malloc(n * sizeof(int*));
    *cs = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        a[i] = (int*)malloc(n * sizeof(int));
        (*cs)[i] = n;
    }

    int t = 0;
    int d = n - 1;
    int l = 0;
    int r = n - 1;
    int x = 1;

    while (t <= d && l <= r) {

        for (int i = l; i <= r; i++)
            a[t][i] = x++;
        t++;

        for (int i = t; i <= d; i++)
            a[i][r] = x++;
        r--;

        if (t <= d) {
            for (int i = r; i >= l; i--)
                a[d][i] = x++;
            d--;
        }

        if (l <= r) {
            for (int i = d; i >= t; i--)
                a[i][l] = x++;
            l++;
        }
    }

    *rs = n;

    return a;
}