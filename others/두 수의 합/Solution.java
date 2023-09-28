import java.util.Arrays;

public class Solution
{
    private String findIdx(int[] lst,int target)
    {
        int[] result = {0,0};
//        System.out.println(Arrays.toString(lst));

        for (int num : lst) {
            int compare = target - num;
            if (num!=compare && Arrays.stream(lst).anyMatch(i -> i == compare) )
            {
                result[0] = num;
                result[1] = compare;
                break;
            }
        }

        Arrays.sort(result);
        return Arrays.toString(result);

    }
    public static void main(String [] args)
    {
//        int[] lst = {7, 3, 2, 13, 9, 15, 8, 11};
//        int target = 12 ;

//        int[] lst = {7, 5, 12, -9, -12, 22, -30, -35, -21};
//        int target = -14 ;

        int[] lst = {7, 5,8, 12, 20};
        int target = 16 ;
        Solution sol = new Solution();

        System.out.print(sol.findIdx(lst,target));
    }
}