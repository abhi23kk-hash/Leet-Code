class Solution {

    List<List<Integer>> a = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] c, int t) {

        Arrays.sort(c);

        f(c, t, 0, new ArrayList<>());

        return a;
    }

    void f(int[] c, int t, int i, List<Integer> b) {

        if (t == 0) {
            a.add(new ArrayList<>(b));
            return;
        }

        for (int j = i; j < c.length; j++) {

            if (j > i && c[j] == c[j - 1])
                continue;

            if (c[j] > t)
                break;

            b.add(c[j]);

            f(c, t - c[j], j + 1, b);

            b.remove(b.size() - 1);
        }
    }
}