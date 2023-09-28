class Solution {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length/n][n];
        
        int idx = 0; 
        for (int i=0; i<num_list.length/n; i++)
            for (int j=0; j<n; j++)
            {
                answer[i][j] = num_list[idx];
                idx++;
                
            }
        return answer;
    }
}

// 다른사람 풀이 
// class Solution {
//     public int[][] solution(int[] num_list, int n) {
//         int length = num_list.length;
//         int[][] answer = new int[length/n][n];
        
//         for(int i=0; i<length; i++){
//             answer[i/n][i%n]=num_list[i];
//         }

//         return answer;
//     }
// }