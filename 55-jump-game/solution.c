bool canJump(int* a, int n) {

    int m = 0;

    for (int i = 0; i < n; i++) {

        if (i > m)
            return false;

        if (i + a[i] > m)
            m = i + a[i];
    }

    return true;
}