import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        int n, m,x1,y1,x2,y2;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int [][] array = new int[n+1][m+1];

        for (int i =1; i<n+1;i++)
        {
            st = new StringTokenizer(br.readLine());
            for(int j =1; j<m+1; j++)
                array[i][j] = Integer.parseInt(st.nextToken());
        }
        
        // 누적합
        for(int i=1; i<n+1; i++) {
            for(int j=1; j<m+1; j++)
                array[i][j] = array[i][j] + array[i-1][j] + array[i][j-1] - array[i-1][j-1];
        }
        int sum_num = Integer.parseInt(br.readLine());
        for (int i =0; i<sum_num ;i++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            System.out.println(array[x2][y2] - array[x1-1][y2] - array[x2][y1-1] + array[x1-1][y1-1]);
        }

    }
}