import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int [][] schedule = new int[num][2];
        int [] dp = new int[num+1];

        for (int i =0; i<num; i++) {
            schedule[i][0] = scan.nextInt();
            schedule[i][1] = scan.nextInt();
        }

        for(int i=0; i<num; i++)
            for(int j= i+schedule[i][0] ; j< num+1 ; j++)
                if (dp[j] < schedule[i][1]+dp[i])
                    dp[j] = schedule[i][1]+dp[i];
        System.out.print(dp[num]);



    }
}