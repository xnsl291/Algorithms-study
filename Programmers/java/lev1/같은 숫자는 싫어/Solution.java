import java.util.Stack;

public class Solution{
    public Stack solution(int []arr) {
        Stack input_arr = new Stack();

        input_arr.push(arr[0]);
        int prev = arr[0];
        for (int i :arr)
            if (prev != i){
                input_arr.push(i);
                prev= i;
            }

        return input_arr;
    }
}