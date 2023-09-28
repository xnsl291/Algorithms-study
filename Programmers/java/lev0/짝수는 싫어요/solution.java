class Solution {
    public int[] solution(int n) {
        int [] answer = new int[ n%2==0 ? (int)n/2 : (int)n/2+1 ];
        for(int idx=0,i =1;i<n+1;i+=2,idx++)
            answer[idx] = i;
        return answer ;
    }
}