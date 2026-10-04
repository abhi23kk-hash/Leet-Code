class Solution {
    public boolean isMatch(String s, String p) {

        int m = s.length();
        int n = p.length();

        boolean[][] a = new boolean[m + 1][n + 1];

        a[0][0] = true;

        for (int j = 1; j <= n; j++) {

            if (p.charAt(j - 1) == '*')
                a[0][j] = a[0][j - 1];
        }

        for (int i = 1; i <= m; i++) {

            for (int j = 1; j <= n; j++) {

                if (p.charAt(j - 1) == '*')
                    a[i][j] = a[i][j - 1] || a[i - 1][j];

                else if (p.charAt(j - 1) == '?' || s.charAt(i - 1) == p.charAt(j - 1))
                    a[i][j] = a[i - 1][j - 1];
            }
        }

        return a[m][n];
    }
}