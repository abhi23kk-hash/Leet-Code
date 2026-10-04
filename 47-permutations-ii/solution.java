class Solution {

    List<List<Integer>> a = new ArrayList<>();

    public List<List<Integer>> permuteUnique(int[] n) {

        Arrays.sort(n);

        boolean[] v = new boolean[n.length];

        f(n, v, new ArrayList<>());

        return a;
    }

    void f(int[] n, boolean[] v, List<Integer> b) {

        if (b.size() == n.length) {
            a.add(new ArrayList<>(b));
            return;
        }

        for (int i = 0; i < n.length; i++) {

            if (v[i])
                continue;

            if (i > 0 && n[i] == n[i - 1] && !v[i - 1])
                continue;

            v[i] = true;
            b.add(n[i]);

            f(n, v, b);

            b.remove(b.size() - 1);
            v[i] = false;
        }
    }
}