class Solution {
    public int solution(int hp) {
        return (int)hp/5 + (int)hp%5/3 + (int)hp%5%3;
    }
}