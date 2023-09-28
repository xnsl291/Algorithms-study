def solution(hp):
    value = hp // 5 + (hp%5)//3 
    remain = hp % 5 % 3
    return value+remain
        
        