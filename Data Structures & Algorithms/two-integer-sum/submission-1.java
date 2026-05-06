class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] res = new int[2];
        int anchor = 0 ;
        HashMap<Integer,Integer> m = new HashMap<>();
        for(int i=0; i<n; i++){
            anchor = target - nums[i];
            if(m.containsKey(anchor)==true){
                res[0]= m.get(anchor);
                res[1]=i;
            }else{
                m.put(nums[i],i);
            }
        }        
        return res;
    }
}
