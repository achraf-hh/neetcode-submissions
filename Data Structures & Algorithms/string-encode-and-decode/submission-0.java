class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s : strs){
            int len = s.length();
            sb.append(len);
            sb.append("]");
            sb.append(s);
        }
        return sb.toString();
    }

       public List<String> decode(String str) {
        int count = 0;
        StringBuilder tempStr = new StringBuilder();
        StringBuilder countStr = new StringBuilder();
        List<String> strs = new ArrayList<>();
        for(int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            if(count !=0){
                tempStr.append(ch);
                count--;
                if(count == 0){
                    strs.add(tempStr.toString());
                    tempStr.setLength(0);
                }
            }else{
                if(ch != ']'){
                    countStr.append(ch);
                }else{
                    count = Integer.parseInt(countStr.toString());
                    countStr.setLength(0);
                    if(count == 0){
                        strs.add("");
                    }
                }
            
        }
    }
    return strs;
}
}
