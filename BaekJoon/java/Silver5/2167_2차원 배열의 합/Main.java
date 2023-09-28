import java.util.*;
public class Main {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int m = scan.nextInt();

        int [][] array = new int[n][m];

        for (int i =0; i<n;i++)
            for(int j =0; j<m; j++)
                array[i][j] = scan.nextInt();

        // 누적합
        for(int i=1; i<n+1; i++) {
            for(int j=1; j<m+1; j++) 
                array[i][j] = array[i][j]+array[i-1][j] + array[i][j-1] - array[i-1][j-1];
        }
        
        int sum_num = scan.nextInt();
        for (int i =0; i<sum_num ;i++) {
            int answer = 0;
            int x1 = scan.nextInt();
            int y1 = scan.nextInt();
            int x2 = scan.nextInt();
            int y2 = scan.nextInt();

        
        System.out.println(array[x2][y2] - array[x2][y1-1] - array[x1-1][y2] + array[x1-1][y1-1])
        }




    }
}
