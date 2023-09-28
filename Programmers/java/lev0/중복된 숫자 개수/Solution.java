class Solution {
    public int solution(int[] arr, int n)
     {
         int cnt = 0;
         for (int i:arr)
             cnt += (i == n)?1:0;
         return cnt;
     }
 }