def solution(number, limit, power):
    answer = 0
    # 1. number까지 각 수의 약수 개수 세기 
    # 2. limit 초과하는지 확인하고 
    # 3. 초과분은 power로 대체 
    # 4. 합 리턴
    cnt = 0
    for i in range(1,number+1):
        cnt += power if getNum(i) > limit else getNum(i)
    return cnt


def getNum(number):
    cnt = 0
    
    for j in range(1, int(number**(1/2))+1):
        if number%j == 0 :
            cnt= cnt+2 if ( (j**2) != number) else cnt+1 

    return cnt

