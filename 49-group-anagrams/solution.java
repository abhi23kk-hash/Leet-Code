class Solution {
    public List<List<String>> groupAnagrams(String[] s) {

        HashMap<String, List<String>> m = new HashMap<>();

        for (String x : s) {

            char[] c = x.toCharArray();
            Arrays.sort(c);

            String k = new String(c);

            if (!m.containsKey(k))
                m.put(k, new ArrayList<>());

            m.get(k).add(x);
        }

        return new ArrayList<>(m.values());
    }
}