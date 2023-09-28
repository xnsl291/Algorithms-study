import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException
    {
        int n,m,i,j,total=0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int [] numbers = new int [n];
        int [] dp = new int[n+1];
        st = new StringTokenizer(br.readLine());

        // numbers 입력 + 누적합
        for(int k =0; k<n; k++ ) {
            numbers[k] = Integer.parseInt(st.nextToken());
            dp[k+1] = dp[k] + numbers[k] ;
        }

        for(int k = 0; k<m; k++) {
            st = new StringTokenizer(br.readLine());
            i = Integer.parseInt(st.nextToken());
            j = Integer.parseInt(st.nextToken());
            System.out.println(dp[j] - dp[i-1]);
        }
    }

}
