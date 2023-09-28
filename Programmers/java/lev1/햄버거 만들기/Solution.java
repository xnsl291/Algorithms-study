import java.util.Stack;

class Solution{
    public int solution(int[] ingredient) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for (int i : ingredient)
        {
            stack.push(i);
            int sz = stack.size();
            
            if (sz>=4 && stack.peek() == 1)
            {

                if (stack.get(sz-2) == 3 && 
                    stack.get(sz-3) == 2 &&
                    stack.get(sz-4) == 1 )
                {
                        answer ++;
                        for(int j = 0; j<4;  j++)
                        stack.pop();
                }
            }
        }


        return answer;
    }


    public static void main(String[] args){
        // int[] ingredient = new int[]{2, 1, 1, 2, 3, 1, 2, 3, 1};
        int[] ingredient = new int[]{1, 3, 2, 1, 2, 1, 3, 1, 2};

        Solution sol = new Solution();
        System.out.println("Answer :: "+sol.solution(ingredient));
    }
}

// // 다른사람 풀이 
// class Solution {
//     public int solution(int[] ingredient) {
//         int[] stack = new int[ingredient.length];
//         int sp = 0;
//         int answer = 0;
//         for (int i : ingredient) {
//             stack[sp++] = i;
//             if (sp >= 4 && stack[sp - 1] == 1
//                 && stack[sp - 2] == 3
//                 && stack[sp - 3] == 2
//                 && stack[sp - 4] == 1) {
//                 sp -= 4;
//                 answer++;
//             }
//         }
//         return answer;
//     }
// }