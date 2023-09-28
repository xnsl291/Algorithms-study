class Solution {
    final static int ICE_COFFEE_PRICE = 5500;
    public int[] solution(int money) {
        return new int[]{money/ICE_COFFEE_PRICE,money%ICE_COFFEE_PRICE};
    }
}