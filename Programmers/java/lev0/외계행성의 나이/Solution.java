class Solution {
    public String solution(int age) {
        String answer = "";
        String str_age = String.valueOf(age);
        
        for (int i=0; i<str_age.length(); i++)
            answer += (char)  (   (int)( str_age.charAt(i) )+1  +'0');

        return answer;
    }
}