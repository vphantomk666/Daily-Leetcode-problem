
class Solution {

    private boolean solve(char[][] board, int row, int col, char d) {

        for (int i = 0; i < 9; i++) {
            if (board[row][i] == d) {
                return false;
            }

            if (board[i][col] == d) {
                return false;
            }
        }

        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;

        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] == d) {
                    return false;
                }
            }
        }

        return true;
    }

    public boolean isValidSudoku(char[][] board) {

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {

                if (board[i][j] == '.') {
                    continue;
                }

                char d = board[i][j];

                board[i][j] = '.';

                boolean valid = solve(board, i, j, d);

                board[i][j] = d;

                if (!valid) {
                    return false;
                }
            }
        }

        return true;
    }
}
