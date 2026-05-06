class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int l = 0, r = n-1;
        List<Integer> res = new ArrayList<>();
        while(l<r){
            if(numbers[l]+numbers[r] > target){
                r--;
            }else if(numbers[l]+numbers[r] < target){
                l++;
            }else{
                res.add(l+1);
                res.add(r+1);
                break;
            }
        }

        return res.stream().mapToInt(i -> i).toArray();
    }
}
