import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String [] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue <Integer> p_queue = new PriorityQueue<>();

        int num = Integer.parseInt(br.readLine());

        for (int i=0; i<num; i++)
            p_queue.add(Integer.parseInt(br.readLine()));

        int answer = 0;
        while(p_queue.size()>1)
        {
            int sum_val = p_queue.poll()+p_queue.poll();
            answer += sum_val;
            p_queue.add(sum_val);
        }

        System.out.print(answer);

    }
}
