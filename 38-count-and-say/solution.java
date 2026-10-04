class Solution {
    public String countAndSay(int n) {

        String s = "1";

        for (int i = 2; i <= n; i++) {

            StringBuilder a = new StringBuilder();

            int c = 1;

            for (int j = 1; j < s.length(); j++) {

                if (s.charAt(j) == s.charAt(j - 1))
                    c++;
                else {
                    a.append(c);
                    a.append(s.charAt(j - 1));
                    c = 1;
                }
            }

            a.append(c);
            a.append(s.charAt(s.length() - 1));

            s = a.toString();
        }

        return s;
    }
}