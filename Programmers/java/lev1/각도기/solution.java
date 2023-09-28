class Solution {
    public int solution(int angle) {
        int answer = ((int)angle/90)*2;
        return answer+ (angle%90>0? 1: 0);
    }
}

// class Solution {
//     public int solution(int angle) {
//         return angle == 180 ? 4 : angle < 90 ? 1 : angle == 90 ? 2 : angle > 90 ? 3 : 0;
//     }
// }