class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for (int i =0 ; i < my_string.length() ; i++)
            for (int j = 0; j<n; j++)
                answer += my_string.charAt(i);
        return answer;
    }
}

/* 다른사람 풀이 1 - string[] + repeat() 사용 
class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] str = my_string.split("");
        for(int i=0; i<my_string.length(); i++){
            answer += str[i].repeat(n);
        }
        return answer;
    }
}
*/

/* 다른사람 풀이 2 StringBuilder + repeat() 사용
class Solution {
    public String solution(String my_string, int n) {
        StringBuilder sb = new StringBuilder();
        for(char c : my_string.toCharArray()){
            sb.append((c + "").repeat(n));
        }
        return sb.toString();
    }
}
*/