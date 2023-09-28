class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i=my_string.length()-1; i>=0; i--){
            answer+=my_string.charAt(i);
        }
        return answer;
        }
}

// StringBuilder 사용하면 쉽게 reverse 할 수 있다
// class Solution {
//     public String solution(String myString) {
//         return new StringBuilder(myString).reverse().toString();
//     }
// }