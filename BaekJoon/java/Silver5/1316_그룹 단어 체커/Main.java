import java.util.*;

public class Main {
    private static int check_word(String word)
    {
        Stack stack = new Stack();
        for(int i=0 ; i<word.length() ; i++)
        {
            char target = word.charAt(i);
            if (!stack.contains(target))
                stack.push(target);

            else if (!String.valueOf(stack.lastElement()).equals(String.valueOf(target)))
                return 0;
        }
        return 1;
    }
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int answer = 0;
        String word ="";
        int num = scan.nextInt();

        for (int i=0 ; i<num ; i++) {
            word = scan.next();
            answer += check_word(word);
        }
        System.out.print(answer);
    }
}