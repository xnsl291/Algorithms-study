import java.math.BigInteger;
class Solution {
    public int solution(int ball, int share) {
        share = Math.max(share, ball-share);
        BigInteger answer= BigInteger.valueOf(1);

          for (int i = ball;i>share ; i--)
              answer = answer.multiply(BigInteger.valueOf(i));
          for (int i = 1;i<=ball-share;i++)
              answer = answer.divide(BigInteger.valueOf(i));

        return answer.intValueExact();
    }
}