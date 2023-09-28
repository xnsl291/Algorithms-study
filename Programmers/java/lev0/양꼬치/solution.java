class Solution {
    static final int MEAT = 12000;
    static final int DRINK = 2000;
    
    public int solution(int n, int k) {
        return MEAT*n + DRINK* (k - (int)(n/10) );
    }
}