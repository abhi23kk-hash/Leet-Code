class Solution {
    public void solveSudoku(char[][] b) {
        solve(b);
    }

    boolean solve(char[][] b) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {

                if (b[i][j] == '.') {

                    for (char c = '1'; c <= '9'; c++) {

                        if (check(b, i, j, c)) {

                            b[i][j] = c;

                            if (solve(b))
                                return true;

                            b[i][j] = '.';
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    boolean check(char[][] b, int r, int c, char x) {

        for (int i = 0; i < 9; i++) {

            if (b[r][i] == x)
                return false;

            if (b[i][c] == x)
                return false;

            if (b[3 * (r / 3) + i / 3][3 * (c / 3) + i % 3] == x)
                return false;
        }

        return true;
    }
}