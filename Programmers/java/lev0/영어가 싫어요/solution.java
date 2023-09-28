class Solution {
    public long solution(String numbers) {
        String [] alpha= new String[] {"zero","one","two","three","four","five","six","seven","eight","nine"};

        for (int i=0;i<alpha.length;i++)
            numbers = numbers.replace(alpha[i],String.valueOf(i)); 
        return Long.parseLong(numbers);
    }
}