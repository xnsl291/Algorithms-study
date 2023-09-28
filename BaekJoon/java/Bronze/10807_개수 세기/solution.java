import java.util.Scanner;
public class solution {
    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int arr_size = sc.nextInt();
    int num_lst[] = new int[arr_size];
    for (int i = 0; i < arr_size; i++)
        num_lst[i] = sc.nextInt();

    int target = sc.nextInt();
    int cnt=0;
    
    for(int i:num_lst)
        if (i == target)
            cnt++;

    System.out.println(cnt);
    sc.close();
    }
}

