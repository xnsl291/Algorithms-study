import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int cnt = 0 , weight = 0;
        Arrays.sort(people);
        
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i : people )
            deque.add(i);
        
        while( deque.size() > 1){
            weight = deque.getFirst()+ deque.getLast();

            if (weight <= limit){
                deque.removeFirst();
                deque.removeLast();
            }
            else if (weight > limit)
                deque.removeLast();

            cnt++;

            if ( deque.size()==1 )
                cnt++;
        }
        return cnt;
    }
}