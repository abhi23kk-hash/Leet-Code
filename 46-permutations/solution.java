class Solution {

    List<List<Integer>> a = new ArrayList<>();

    public List<List<Integer>> permute(int[] n) {
        f(n, 0);
        return a;
    }

    void f(int[] n, int i) {

        if (i == n.length) {

            List<Integer> b = new ArrayList<>();

            for (int x : n)
                b.add(x);

            a.add(b);
            return;
        }

        for (int j = i; j < n.length; j++) {

            int t = n[i];
            n[i] = n[j];
            n[j] = t;

            f(n, i + 1);

            t = n[i];
            n[i] = n[j];
            n[j] = t;
        }
    }
}