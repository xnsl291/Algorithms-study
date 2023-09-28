import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String,Integer> map = new HashMap<>();
        int[] answer = new int[photo.length];
        for (int i=0 ; i<name.length; i++)
            map.put(name[i],yearning[i]);

        for( int i =0 ; i< photo.length; i++)
        {
            int point = 0 ;
            for (String person : photo[i])
                point += map.getOrDefault(person,0);
            answer[i] = point;
        }
        return answer;
    }

    public static void main(String[] args)
    {
        Solution t = new Solution();

        String[] name = {"may", "kein", "kain", "radi"};
        int[] yearning = {5, 10, 1, 3};
        String[][] photo = {{"may", "kein", "kain", "radi"},{"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};
        System.out.println(t.solution(name, yearning,photo));
    }
}