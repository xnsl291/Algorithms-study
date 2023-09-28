import java.util.Arrays;
import java.util.Collections;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // int[] 내림차순 정렬 
        Integer[] array = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(array, Collections.reverseOrder());
        
        for (int i =1 ; i<=array.length; i++)
            if (array[i-1] >= i )
                answer++;
        return answer;
    }
}