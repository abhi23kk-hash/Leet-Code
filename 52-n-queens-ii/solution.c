int a[10], n, ans;

int ok(int r, int c) {
    for (int i = 0; i < r; i++)
        if (a[i] == c || abs(a[i] - c) == abs(i - r))
            return 0;

    return 1;
}

void f(int r) {

    if (r == n) {
        ans++;
        return;
    }

    for (int c = 0; c < n; c++) {

        if (ok(r, c)) {
            a[r] = c;
            f(r + 1);
        }
    }
}

int totalNQueens(int x) {

    n = x;
    ans = 0;

    f(0);

    return ans;
}