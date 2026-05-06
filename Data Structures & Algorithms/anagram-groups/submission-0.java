class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        int m = strs.length;
        Map<String,List<String>> map = new HashMap<>();
        for(int i=0; i<m; i++){
            int n = strs[i].length();
            int[] freq = new int[26]; 
            for(int j=0; j<n; j++){
                char ch  = strs[i].charAt(j);
                freq[ch - 'a']++;
            }
            String str = Arrays.toString(freq);
            if(map.containsKey(str)==false){
                map.put(str, new ArrayList<>(Arrays.asList(strs[i])) );
            }else{
                map.get(str).add(strs[i]);
            }
            

        }
        res.addAll(map.values());
        return res;
    }
}
