class Solution {
    public int[] productExceptSelf(int[] nums) {
      int[] output = new int[nums.length];
      Arrays.fill(output,1); 
      int i = 0;
      while(i < nums.length){
        for(int j = 0; j < i; j++){
            int left_prod = 1;
            left_prod = left_prod * nums[j];
            output[i] = output[i]*left_prod;
        }
        for(int j = i+1; j < nums.length ; j++){
            int right_prod = 1;
            right_prod = right_prod * nums[j];
            output[i] = output[i]*right_prod;
        }
        i++;
      }
      return output;
    }
}  
