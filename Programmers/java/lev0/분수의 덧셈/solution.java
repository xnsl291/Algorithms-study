class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {(numer1 *denom2 + numer2*denom1) , (denom1 * denom2) } ;
        int num = answer[0]>answer[1]?answer[0]:answer[1];
        for (int i =(int)num/2 ; i>1;i--)
            if (answer[0]%i ==0 && answer[1]%i ==0)
            {
                answer [0] = (int)answer[0]/i;
                answer[1] = (int)answer[1]/i;
            }
                
        return answer;
        
    }
}