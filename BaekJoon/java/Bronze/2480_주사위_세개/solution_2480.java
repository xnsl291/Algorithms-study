// from collections import Counter
// numbers = Counter(list(map(int,input().split())))

// def solv(numbers):
//     if len(numbers.keys())==1:
//         return 10000+list(numbers.keys())[0]*1000
//     elif len(numbers.keys())==2:
//         return 1000+(numbers.most_common()[0][0])*100
//     else:
//         return (max(numbers.items())[0])*100

// print(solv(numbers))
package JAVA.pg_bronze.주사위_세개_2480;
import java.util.Scanner;
public class solution_2480
{
    static Scanner sc = new Scanner(System.in);
// 딕셔너리화 해서 키의 개수 세면서 풀면 될 것같음
    static int verified()
    {
        int type=0;
        return type;
    }
    public static void main(String[] args)
    {
        num1 = sc.nextInt();
        num2 = sc.nextInt();
        num3 = sc.nextInt();
        System.out.printf("%d %d %d\n",num1,num2,num3);
        System.out.println(verified());
    }
}

