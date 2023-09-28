import java.util.Arrays;
import java.util.Scanner;

public class Main{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr_size = sc.nextInt();
        int num_lst[] = new int[arr_size];
        for (int i = 0; i < arr_size; i++)
            num_lst[i] = sc.nextInt();

        Arrays.sort(num_lst);

        System.out.printf("%d %d",num_lst[0],num_lst[arr_size-1]);
        sc.close();
    }
}

