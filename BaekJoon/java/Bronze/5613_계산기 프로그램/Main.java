import java.util.*;
public class Main {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int num = 0;
        String cal = "";
        int answer = scan.nextInt();
        
        while(true)
        {
            cal = scan.next();
            if (cal.equals("=")) {
                System.out.println(answer);
                break;
            }
            num = scan.nextInt();

            switch(cal)
            {
                case "+" :  answer += num; break;
                case "-" :  answer -= num; break;
                case "/" :  answer = (int) answer/num; break;
                case "*" :  answer *= num; break;
            }
        }
    }
}