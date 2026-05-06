class Solution {
    public int maxArea(int[] heights) {
        int  l = 0, r = heights.length - 1;
        int area = 0;
        while(l < r){
            int current_area = (r-l) * Math.min(heights[l], heights[r]);
            if(current_area > area){
                area = current_area;
            }
            if(heights[l] > heights[r]){
                r--;
            }else{
                l++;
            }
        }
        return area;
    }
}
