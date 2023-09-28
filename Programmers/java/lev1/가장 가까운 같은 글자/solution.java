class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        for(int i=0;i<s.length();i++){
            String tmp_str = s.substring(0,i);
            
            if(tmp_str.indexOf(s.charAt(i)) >=0) 
                answer[i] = i - tmp_str.lastIndexOf(s.charAt(i));
            else
                answer[i] = -1;      
        }
        return answer;
    }
}