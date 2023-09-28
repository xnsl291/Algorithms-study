import java.io.BufferedReader;
// import java.io.BufferedWriter;
import java.io.InputStreamReader;
// import java.io.OutputStreamWriter;
import java.io.IOException; 

public class solution_2743
{
    public static void main(String[] args) throws IOException 
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String target = br.readLine();
        br.close(); 
        // BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        // bw.write(target.length());   
        // bw.close();  
        System.out.println(target.length());
    }
}