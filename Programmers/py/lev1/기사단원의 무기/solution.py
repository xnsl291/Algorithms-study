def solution(number, limit, power):
    answer = 0
    # 1. number까지 각 수의 약수 개수 세기 
    # 2. limit 초과하는지 확인하고 
    # 3. 초과분은 power로 대체 
    # 4. 합 리턴
    cnt = 0
    for i in range(1, int (number/2)+1):
        print(i,"의 약수 개수 구하기")
        cnt += power if getNum(i) > limit else getNum(i)
        print("-------------------")

    return cnt*2


def getNum(number):
    cnt = 0
    
    for j in range(1, int(number**(1/2))+1):
        if number%j == 0 :
            cnt= cnt+2 if ( (j**2) != number) else cnt+1 
            print("j = ",j," cnt = ",cnt)
    return cnt

print(solution(5,3,2)) #203