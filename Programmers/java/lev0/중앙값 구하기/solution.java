import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        return array[(int)array.length/2];
    }
}