class Solution {
    public int solution(int price) {
        price *= price >=500000? 0.8 : price >=300000? 0.9 : price>=100000? 0.95 : 1;
        return price;
    }
}