class Solution {
public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++){
            int l = i+1, r = nums.length - 1;
            if(i>0 && nums[i] == nums[i-1]) continue;
            while(l<r){
                int target = nums[i] + nums[l] + nums[r];
                if(target > 0) r--;
                else if(target<0) l++;
                else{
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    while(nums[l] == nums[l-1] && l<r){
                        l++;
                    }
                }
            }
        }
        return res;
    }
}
