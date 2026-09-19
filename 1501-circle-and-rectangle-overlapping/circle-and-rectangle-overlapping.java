class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closest_x = Math.max(x1,Math.min(x2, xCenter));
        int closest_y = Math.max(y1,Math.min(y2, yCenter));

        int distX = xCenter - closest_x;
        int distY = yCenter - closest_y;
        int overlapping_dist = (distX * distX) + (distY * distY);

        return overlapping_dist <= (radius*radius);
    }
}