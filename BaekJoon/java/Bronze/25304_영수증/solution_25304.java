import java.util.Scanner;
public class solution_25304 {
    static int total_price, howMany,price_sum;
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        total_price = scan.nextInt();
        howMany = scan.nextInt();
        
        for(int i=0;i<howMany;i++)
        {
            int price = scan.nextInt();
            int num = scan.nextInt();
            price_sum+=(price*num);
        }
        if (price_sum==total_price)
            System.out.println("Yes");
        else
            System.out.println("No");

        scan.close();
    }
}
