import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.LinkedList;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Character,Integer> map = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        String[] input_arr = new String[n];

        for(int i =0; i<n; i++)
        {
            String input = br.readLine();
            for(int j=input.length()-1; j>=0; j--) {
                char key = input.charAt(input.length() - 1 - j);
                if(!map.containsKey(key))
                    map.put(key, (int)Math.pow(10,j));
                else
                    map.put(key, map.get(key) + (int)Math.pow(10,j));
            }
            input_arr[i] = input;
        }

        // 요소 정렬
        List<Map.Entry<Character, Integer>> entryList = new LinkedList<>(map.entrySet());
        entryList.sort(new Comparator<Map.Entry<Character, Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> o1, Map.Entry<Character, Integer> o2) {
                return o2.getValue() - o1.getValue();
            }
        });

        //map 요소 중, 값이 큰 순서대로 9~ 값 부여하기
        int idx = 9;
        for(Map.Entry<Character, Integer> entry : entryList){
            map.put(entry.getKey(), idx) ;// 덮어쓰기
            idx --;
        }

        int answer = 0 ;
        // 값 대체
        for(String str:input_arr)
            for (int j=str.length()-1; j>=0; j--)
                answer += map.get(str.charAt(str.length()-1-j))   *Math.pow(10,j) ;
        System.out.println(answer);

    }
}