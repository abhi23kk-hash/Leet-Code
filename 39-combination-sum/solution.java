class Solution {

    List<List<Integer>> a = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] c, int t) {
        f(c, t, 0, new ArrayList<>());
        return a;
    }

    void f(int[] c, int t, int i, List<Integer> b) {

        if (t == 0) {
            a.add(new ArrayList<>(b));
            return;
        }

        if (i == c.length || t < 0)
            return;

        b.add(c[i]);
        f(c, t - c[i], i, b);
        b.remove(b.size() - 1);

        f(c, t, i + 1, b);
    }
}