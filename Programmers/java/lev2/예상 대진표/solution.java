// 파이썬 코드 참고 
class Solution
{
    public int solution(int n, int a, int b)
    {
        return Integer.toBinaryString((a-1)^(b-1)).length() ;
    }
}

// 내 코드
class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer =0 ;
        while(a != b)
        {
            a = (int)(a+1)/2;
            b = (int)(b+1)/2;
            answer++;
        }
        return answer;
    }
}