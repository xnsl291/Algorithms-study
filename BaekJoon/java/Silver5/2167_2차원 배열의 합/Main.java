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

        int sum_num = scan.nextInt();
        for (int i =0; i<sum_num ;i++) {
            int answer = 0;
            int x1 = scan.nextInt();
            int y1 = scan.nextInt();
            int x2 = scan.nextInt();
            int y2 = scan.nextInt();

            for (int val1 = x1; val1<x2+1;val1++)
                for(int val2 = y1; val2 < y2+1; val2++)
                    answer += array[val1 - 1][val2 - 1];
            System.out.println(answer);
        }




    }
}
