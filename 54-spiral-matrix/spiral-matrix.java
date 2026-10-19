
import java.util.*;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        int left = 0;
        int right = m - 1;
        int top = 0;
        int bottom = n - 1;

        List<Integer> res = new ArrayList<>();

        while (left <= right && top <= bottom) {

            // Traverse left to right
            for (int j = left; j <= right; j++) {
                res.add(matrix[top][j]);
            }
            top++;

            // Traverse top to bottom
            for (int i = top; i <= bottom; i++) {
                res.add(matrix[i][right]);
            }
            right--;

            // Traverse right to left
            if (top <= bottom) {
                for (int j = right; j >= left; j--) {
                    res.add(matrix[bottom][j]);
                }
                bottom--;
            }

            // Traverse bottom to top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    res.add(matrix[i][left]);
                }
                left++;
            }
        }

        return res;
    }
}
