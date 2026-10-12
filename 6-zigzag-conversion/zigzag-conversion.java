class Solution {
    public String convert(String s, int numRows) {
        int n = s.length();

        if (numRows == 1 || n <= numRows) {
            return s;
        }

        String[][] zigzag = new String[numRows][n];

        int row = 0;
        int col = 0;
        boolean down = true;

        for (char ch : s.toCharArray()) {
            zigzag[row][col] = String.valueOf(ch);

            if (down) {
                if (row == numRows - 1) {
                    down = false;
                    row--;
                    col++;
                } else {
                    row++;
                }
            } else {
                if (row == 0) {
                    down = true;
                    row++;
                } else {
                    row--;
                    col++;
                }
            }
        }

        StringBuilder result = new StringBuilder();

        for (String[] r : zigzag) {
            for (String ch : r) {
                if (ch != null) {
                    result.append(ch);
                }
            }
        }

        return result.toString();
    }
}
