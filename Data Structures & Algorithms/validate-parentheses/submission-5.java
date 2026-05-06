class Solution {
       public boolean isValid(String s){
        Deque<Character> stack = new ArrayDeque<>();

        if(s.length() % 2 != 0 ) return false;

        boolean c = false;

        for(int i = 0; i < s.length(); i++ ){
            if(s.charAt(i) == '(' | s.charAt(i) == '[' | s.charAt(i) == '{') {
                stack.addFirst(s.charAt(i));
                
            };
            if(s.charAt(i) == ')'){
                if(stack.isEmpty() ==false && stack.getFirst() == '(') stack.pop();
                else return false;
            }
            if( s.charAt(i) == ']'){
                if(stack.isEmpty() ==false && stack.getFirst() == '[') stack.pop();
                else return false;
            }
            if(s.charAt(i) == '}'){
                if(stack.isEmpty() ==false && stack.getFirst() == '{') stack.pop();
                else return false;
            }

            
        
        

        }
        if(stack.isEmpty() == true) c = true;

        return c;
    }

}
