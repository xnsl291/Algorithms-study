import sys
# https://www.acmicpc.net/board/view/25689 문제 설명 (참고사이트)

def solution(): 
    input = int(sys.stdin.readline())
    result = []
    # 한자리 수 일경우 
    if input <10 and input >0:
        cnt = input

    # 두자리 수 이상 
    else:
        cnt = 9
        for j in range(10,input+1):
            flag = 0
            # 각 자리의 수의 합/차가 일정할 경우 
            tmp_lst = [ int(i) for i in str(j)]
            result = [ tmp_lst[i]-tmp_lst[i+1] for i in range(len(tmp_lst)-1)]
            if len(set(result)) == 1:
            # 조건에 맞는다면 카운드 증강
                cnt+=1

    # 한수의 개수 출력 
    return cnt

print(solution())