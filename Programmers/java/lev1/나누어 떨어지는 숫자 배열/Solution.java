import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    public static ArrayList solution(int[] arr,int divisor )
    {
        ArrayList answer = new ArrayList();
        for (int i: arr)
            if (i%divisor == 0)
                answer.add(i);

        if (answer.isEmpty())
            answer.add(-1);
        else
            Collections.sort(answer);
        return answer;
    }
}
