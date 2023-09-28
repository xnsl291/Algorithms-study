class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String [n];
        String value = "";
        
        for (int i =0; i<n;i++)
        {
            value = String.format( "%"+n+"s", Integer.toBinaryString( arr1[i] | arr2[i] ) );
            answer[i] = value.replace("1","#").replace("0"," ");
        }
        
        return answer;
    }
}