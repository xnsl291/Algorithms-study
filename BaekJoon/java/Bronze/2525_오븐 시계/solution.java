import java.util.Scanner;
public class solution {
    public static void main(String[] args) {
        int hour,min,require;
        Scanner sc = new Scanner(System.in);
        hour = sc.nextInt();
        min = sc.nextInt();
        require = sc.nextInt();

        if (min+require>59)
        {
            hour+=((min+require)/60);
            min = (min+require)%60;
            if (hour>23)
                hour-=24;
        }
        else
            min+=require;
        
        System.out.printf("%d:%d",hour,min);
        sc.close();
    }
}



