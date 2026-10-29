
class Solution {

    private int countNei(int[][] board, int r, int c, int row, int col) {
        int nei = 0;

        for (int i = r - 1; i < r + 2; i++) {
            for (int j = c - 1; j < c + 2; j++) {

                if (i < 0 || i >= row || j < 0 || j >= col
                        || (i == r && j == c)) {
                    continue;
                }

                if (board[i][j] == 1 || board[i][j] == 3) {
                    nei++;
                }
            }
        }

        return nei;
    }

    public void gameOfLife(int[][] board) {
        int row = board.length;
        int col = board[0].length;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {

                int nei = countNei(board, r, c, row, col);

                if (board[r][c] == 1) {
                    if (nei < 2 || nei > 3) {
                        board[r][c] = 3; 
                    }
                } else {
                    if (nei == 3) {
                        board[r][c] = 2; 
                    }
                }
            }
        }

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (board[r][c] == 3) {
                    board[r][c] = 0;
                } else if (board[r][c] == 2) {
                    board[r][c] = 1;
                }
            }
        }
    }
}
