class Solution {
    public int solution(String t, String p) {
        String sliced_str ;
        int cnt=0;
        
        for (int i =0; i<t.length()-p.length()+1;i++)
        {
            sliced_str = t.substring(i,i+p.length());
            if (Long.parseLong(sliced_str) <= Long.parseLong(p))
                cnt++;
        }
       
        
        return cnt;
    }
}