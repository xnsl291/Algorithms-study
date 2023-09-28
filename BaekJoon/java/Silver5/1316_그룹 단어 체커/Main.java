import java.util.Scanner;
import java.util.Stack;

public class Main {
    private static int check_word(String word)
    {
        Stack stack = new Stack();
        String [] word_arr = word.split("");
        
        for(String i : word_arr)
        {
            if (!stack.contains(i))
                stack.push(i);
            else if (!i.equals(stack.lastElement()))
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