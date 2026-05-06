class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n != m){
            return false;
        }else{
            List<Character> ch= new ArrayList<>();
            List<Character> st= new ArrayList<>();
            for(int i =0; i<n; i++){
                ch.add(s.charAt(i));
                Collections.sort(ch);
            }
            for(int j = 0; j<m; j++){
                st.add(t.charAt(j));
                Collections.sort(st);
            }
            if(ch.equals(st)){
                return true;
            }else{return false;}
        }
    }
}
