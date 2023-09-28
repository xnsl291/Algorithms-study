import java.util.Arrays;
class Solution{
    public int solution(int k, int[] tangerine) {
        int cnt = 0;
        Arrays.sort(tangerine);
        int[] lst = new int[ tangerine[tangerine.length-1] ];

        for (int i : tangerine)
            lst[i-1] ++;
        
        Arrays.sort(lst);
        
        for (int i = lst.length-1 ; i>=0; i--){
            k -= lst[i];
            cnt ++;
            
            if( k <= 0)
                break;
        }
        
        return cnt;
    }

    public static void main(){
        Solution sol = new Solution();
        int k = 6;
        int [] tangerine = new int[]{1, 3, 2, 5, 4, 5, 2, 3};
        sol.solution(k, tangerine);
    }
}