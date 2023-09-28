import java.util.HashMap;
import java.util.Map;

public class Solution
{
    private int findIdx(String str)
    {
        HashMap<Character,Integer> map = new HashMap<>();
        int tmp_idx,idx=100;
        for (Character c:str.toCharArray())
             map.put(c , map.getOrDefault(c,0)+1);

        for (Map.Entry<Character, Integer> set : map.entrySet())
            if (set.getValue() == 1) {
                tmp_idx = str.indexOf(set.getKey());
                idx = idx > tmp_idx ? tmp_idx : idx;
            }

        return idx!=100 ? idx : -1;

    }
    public static void main(String [] args)
    {
        String str = "teachertimeachest";
        Solution sol = new Solution();

        System.out.print(sol.findIdx(str));
    }
}