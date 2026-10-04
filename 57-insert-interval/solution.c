/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int** insert(int** a, int n, int* c, int* x, int xs, int* rs, int** rcs) {

    int** b = (int**)malloc((n + 1) * sizeof(int*));
    *rcs = (int*)malloc((n + 1) * sizeof(int));

    int k = 0;
    int i = 0;

    while (i < n && a[i][1] < x[0]) {
        b[k] = a[i];
        (*rcs)[k++] = 2;
        i++;
    }

    while (i < n && a[i][0] <= x[1]) {
        if (a[i][0] < x[0])
            x[0] = a[i][0];

        if (a[i][1] > x[1])
            x[1] = a[i][1];

        i++;
    }

    b[k] = (int*)malloc(2 * sizeof(int));
    b[k][0] = x[0];
    b[k][1] = x[1];
    (*rcs)[k++] = 2;

    while (i < n) {
        b[k] = a[i];
        (*rcs)[k++] = 2;
        i++;
    }

    *rs = k;

    return b;
}