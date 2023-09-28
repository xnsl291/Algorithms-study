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