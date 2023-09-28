import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException
    {
        int n,m,x1,x2,y1,y2;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int [][] dp = new int [n+1][n+1];

        for (int k=1; k<n+1; k++) {
            st = new StringTokenizer(br.readLine());
            int row_sum = 0;
            for (int p = 1; p < n+1; p++) {
                row_sum += Integer.parseInt(st.nextToken());
                dp[k][p] = dp[k-1][p]+ row_sum  ;
            }
        }

        for (int k =0; k<m ;k++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            System.out.println(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]);
        }
    }
}