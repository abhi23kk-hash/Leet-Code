class Solution {
    public String multiply(String a, String b) {

        if (a.equals("0") || b.equals("0"))
            return "0";

        int[] c = new int[a.length() + b.length()];

        for (int i = a.length() - 1; i >= 0; i--) {

            for (int j = b.length() - 1; j >= 0; j--) {

                int m = (a.charAt(i) - '0') * (b.charAt(j) - '0');

                int s = m + c[i + j + 1];

                c[i + j + 1] = s % 10;
                c[i + j] += s / 10;
            }
        }

        StringBuilder d = new StringBuilder();

        for (int x : c) {

            if (!(d.length() == 0 && x == 0))
                d.append(x);
        }

        return d.toString();
    }
}