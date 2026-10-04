int a[10], n;
char*** ans;
int* col;
int sz = 0;

int ok(int r, int c) {
    for (int i = 0; i < r; i++) {
        if (a[i] == c || abs(a[i] - c) == abs(i - r))
            return 0;
    }
    return 1;
}

void f(int r) {
    if (r == n) {
        ans[sz] = (char**)malloc(n * sizeof(char*));

        for (int i = 0; i < n; i++) {
            ans[sz][i] = (char*)malloc(n + 1);

            for (int j = 0; j < n; j++)
                ans[sz][i][j] = '.';

            ans[sz][i][n] = '\0';
            ans[sz][i][a[i]] = 'Q';
        }

        sz++;
        return;
    }

    for (int c = 0; c < n; c++) {
        if (ok(r, c)) {
            a[r] = c;
            f(r + 1);
        }
    }
}

char*** solveNQueens(int x, int* rs, int** cs) {

    n = x;
    sz = 0;

    ans = (char***)malloc(400 * sizeof(char**));
    col = (int*)malloc(400 * sizeof(int));

    f(0);

    for (int i = 0; i < sz; i++)
        col[i] = n;

    *rs = sz;
    *cs = col;

    return ans;
}