class Solution {
    final static int PIECE_NUM = 6;
    public int solution(int n) {
        int cnt =0, i =1;
        
        while (( PIECE_NUM * i) %n != 0 )
        {
            i++;
            cnt++;
        }
        return cnt+1;
    }
}

