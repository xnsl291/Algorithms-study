def solution(n, k):
    MEAT = 12000
    DRINK = 2000
    return n*MEAT + DRINK*(k - n//10)