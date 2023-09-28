import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        HashMap <Integer,Integer> map = new HashMap<>();
        int [] emer_copy = emergency.clone();
        int idx = emergency.length-1;
        Arrays.sort(emer_copy);
        
        for ( int i : emer_copy )
        { 
            map.put(i,idx);
            idx --;
        }
        
        for (int i = 0; i<emergency.length ; i++)
           answer[i] = map.get(emergency[i])+1;
        
        return answer;
    }
}



// 다른 사람 풀이 :stream 활용 
// import java.util.Arrays;
// import java.util.Comparator;
// import java.util.stream.Collectors;

// class Solution {
//     public int[] solution(int[] e) {
//         return Arrays.stream(e).map(i -> Arrays.stream(e).boxed().sorted(Comparator.reverseOrder()).collect(Collectors.toList()).indexOf(i) + 1).toArray();
//     }
// }