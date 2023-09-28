class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int [2];
        for (int i: num_list)
            if ( i%2 == 0 )
                answer[0]++;
            else
                answer[1]++;
        return answer;
    }
}

// 다른 사람 풀이 
// class Solution {
//     public int[] solution(int[] num_list) {
//         int[] answer = new int [2];
//         for(int i = 0; i < num_list.length; i++)
//             answer[num_list[i] % 2]++;
//         return answer;
//     }
// }