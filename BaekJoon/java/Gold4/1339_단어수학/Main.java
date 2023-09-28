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
                map.put( key, (map.get(key)!=null?map.get(key):0 ) +(int)Math.pow(10,j) );
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

        int answer = 0;
        int idx = 9;
        for (Map.Entry<Character, Integer> entry : entryList) {
            answer += map.get(entry.getKey()) * idx;
            idx--;
        }
        System.out.println(answer);

    }
}