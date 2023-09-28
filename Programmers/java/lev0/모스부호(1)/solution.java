/*  SOLUTION 1. FOR LOOP 사용
class Solution {
    static final String[] ALPHA_ARR = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    public String solution(String letter) {
        String[] letter_arr = letter.split(" ");
        String answer ="";

        for (int i = 0; i< letter_arr.length; i++)
            for(int j=0;j< ALPHA_ARR.length;j++)
                if (letter_arr[i].equals( ALPHA_ARR[j]))
                    answer += String.format("%c",97+j);
        return answer;
    }
}
*/

// SOLUTION2. HASH MAP 사용
import java.util.HashMap;
import java.util.Map;
class Solution {
    static final String[] ALPHA_ARR = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

    public String solution(String letter) {
        String[] letter_arr = letter.split(" ");
        String answer ="";

        Map<String, String> ht = new HashMap<String, String>();
        for (int i =0;i< ALPHA_ARR.length;i++)
            ht.put(ALPHA_ARR[i], String.format("%c",97+i) );

        for(String str:letter_arr)
            answer+= ht.get(str);

        return answer;
    
    }
}