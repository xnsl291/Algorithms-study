class Solution {
    public int solution(int[] dot) {
        int[][] quad = {{3,2},{4,1}};
        return quad[ dot[0]>0?1:0 ][ dot[1]>0?1:0 ];
    }
}