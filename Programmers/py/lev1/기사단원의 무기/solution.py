# 시간 초과로 테스트케이스 실패 -- 수정요망 

def solution(number, limit, power):
    answer = 0
    # 1. number까지 각 수의 약수 개수 세기 
    # 2. limit 초과하는지 확인하고 
    # 3. 초과분은 power로 대체 
    # 4. 합 리턴
    lst = [] 
    for i in range(1,number+1):
        cnt = 1
        for j in range(1,i):
                cnt+=1 if i%j == 0 else +0
        lst.append(power if cnt > limit else cnt)

    return sum(lst)
