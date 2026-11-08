class Solution {

    int cnt = 0;


    private boolean isConnected(int[][] grid, int row, int col, int n, int m){
        int rowCnt = 0;
        int colCnt = 0;

        for(int i=0; i<m; i++){
            rowCnt += grid[row][i]; 
        }

        for(int j=0; j<n; j++){
            colCnt += grid[j][col];
        }

        return rowCnt > 1 || colCnt > 1;

    }

    public int countServers(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){

                if (grid[i][j] == 1 && isConnected(grid, i, j, n, m)){
                    cnt++;
                }
            }
        }

        return cnt;
    }
}