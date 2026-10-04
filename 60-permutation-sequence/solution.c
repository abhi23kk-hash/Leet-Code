char* getPermutation(int n, int k) {

    int f[10];
    int v[10] = {0};

    f[0] = 1;

    for (int i = 1; i <= n; i++)
        f[i] = f[i - 1] * i;

    char* s = (char*)malloc((n + 1) * sizeof(char));

    k--;

    for (int i = 0; i < n; i++) {

        int x = k / f[n - i - 1];
        k %= f[n - i - 1];

        int c = 0;

        for (int j = 1; j <= n; j++) {

            if (!v[j]) {

                if (c == x) {
                    s[i] = j + '0';
                    v[j] = 1;
                    break;
                }

                c++;
            }
        }
    }

    s[n] = '\0';

    return s;
}