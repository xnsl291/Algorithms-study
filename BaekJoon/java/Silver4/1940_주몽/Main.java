//import java.util.Scanner;
//public class Main {
//
//    public static void main(String[] args) {
//        Scanner scan = new Scanner(System.in);
//        int num = scan.nextInt();
////        for(int i = 0; i <num; i++)
////            System.out.println(judgement(scan.next()));
//    }
//}

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = 0 ;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        HashSet<Integer> set = new HashSet<Integer>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i=0 ; i<n; i++)
            set.add(Integer.parseInt(st.nextToken()));
        
        for(int i : set)
            if (set.contains(m-i))
                cnt ++;
        
        System.out.print(cnt/2);

    }
}