class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;

      for(int i = 0 ; i < n ; i++){
        Set<Character> row = new HashSet<>();
        Set<Character> column = new HashSet<>();
        Set<Character> square = new HashSet<>();

        for(int j = 0; j < n; j++){
            if(board[i][j] != '.' && !row.add(board[i][j])){
                return false;
            }
        }
        for(int j = 0; j < n; j++ ){
            if(board[j][i] != '.' && !column.add(board[j][i])){
                return false;
            }
        }
        int startRow = (i/3)*3;
        int startCol = (i%3)*3;
        for(int r = startRow; r < startRow+3; r++){
            for(int c = startCol; c < startCol+3; c++){
                if(board[r][c] != '.' && !square.add(board[r][c])){
                    return false;
                }
            }
        }
      }


        return true;
    }
}
