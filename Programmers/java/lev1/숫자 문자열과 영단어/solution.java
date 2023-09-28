class Solution {
    static final String[] num_list = { "zero","one","two","three","four","five","six","seven","eight","nine"};
    
    public int solution(String input) 
    {    
        for(int i =0; i<num_list.length;i++)
            input = input.replace(num_list[i],i+"");
        return Integer.parseInt(input);
    }
}