import java.util.Arrays;
class Solution {
    public double solution(int[] numbers) {
        return (double)Arrays.stream(numbers).sum() / numbers.length;
    }
}