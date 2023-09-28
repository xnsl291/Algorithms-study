import java.util.*;

class Solution {
    public int solution(int[] array) {
        HashMap<Integer, Integer> map = new HashMap<>();

        //빈도 카운트
        for (int i : array)
            map.put(i, map.getOrDefault(i, 0) + 1);

        int answer = 0, max_val = 0;

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > max_val) {
                answer = entry.getKey();
                max_val = entry.getValue();
            } else if (max_val == entry.getValue())
                answer = -1;
        }
        return answer;
    }

/*
* 다른사람 풀이 : 거의 비슷. 나는 map을 만들어서 추가한 뒤 entryset활용하여 비교하는 반면
* 아래 코드는 한 for문에서 빈도 계산 후, 비교하고있음. 좀더 깔끔
import java.util.*;
class Solution {
    public int solution(int[] array) {
        int maxCount = 0;
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int number : array){
            int count = map.getOrDefault(number, 0) + 1;
            if(count > maxCount){
                maxCount = count;
                answer = number;
            }
            else  if(count == maxCount){
                answer = -1;
            }
            map.put(number, count);
        }
        return answer;
    }
}
*/

/*
* 다른사람 풀이 2: EntrySet대신, List에 map구조를 추가해서 (내림차순)정렬.
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new LinkedHashMap<>();

        for (int num : array) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(map.entrySet());
        entries.sort((o1, o2) -> o2.getValue() - o1.getValue());

        if (entries.size() > 1) {
            if (entries.get(0).getValue() == entries.get(1).getValue()) return -1;
        }

        return entries.get(0).getKey();
    }
}
*/

    public static void main(String[] args)
    {
        Solution t = new Solution();

        int[] array= {1,1, 2,2, 3, 3, 3, 4}; //3
//        int[] array= {1,1,2,2}; //-1
//        int[] array= {1};  //1
        System.out.println(t.solution(array));
    }
}