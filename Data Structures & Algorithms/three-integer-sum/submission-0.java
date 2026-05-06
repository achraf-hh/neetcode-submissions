class Solution {
public List<List<Integer>> threeSum(int[] nums) {
        HashSet<List<Integer>> s = new HashSet<>();
        int n = nums.length;
        int l = 0, r = n-1;
        Arrays.sort(nums);
        for(int j = 1; j < n; j++){
            while(l<j && j<r){
                int current_sum = nums[l] + nums[r];
                if(current_sum + nums[j] == 0){
                    s.add(java.util.Arrays.asList(nums[r], nums[j], nums[l]));
                    l++;
                    r--;
                }
                else if(current_sum + nums[j]>0){
                    r--;
                }else{
                    l++;
                }
            }
            l = 0;
            r = n-1;
        }


        List<List<Integer>> res = new ArrayList<>(s);
        return res;
    }
}
