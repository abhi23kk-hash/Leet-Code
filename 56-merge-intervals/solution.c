/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int cmp(const void *a, const void *b) {
    return (*(int **)a)[0] - (*(int **)b)[0];
}

int** merge(int** a, int n, int* c, int* rs, int** rcs) {

    qsort(a, n, sizeof(int*), cmp);

    int** b = (int**)malloc(n * sizeof(int*));
    *rcs = (int*)malloc(n * sizeof(int));

    int k = 0;

    b[0] = (int*)malloc(2 * sizeof(int));
    b[0][0] = a[0][0];
    b[0][1] = a[0][1];
    (*rcs)[0] = 2;

    for (int i = 1; i < n; i++) {

        if (a[i][0] <= b[k][1]) {

            if (a[i][1] > b[k][1])
                b[k][1] = a[i][1];

        } else {

            k++;
            b[k] = (int*)malloc(2 * sizeof(int));
            b[k][0] = a[i][0];
            b[k][1] = a[i][1];
            (*rcs)[k] = 2;
        }
    }

    *rs = k + 1;

    return b;
}