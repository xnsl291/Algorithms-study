def solution(left, right):
    result = 0
    for i in range(left, right+1):
        result = result+i if getNum(i)%2==0 else result-i
    return result

def getNum(num): # num의 약수의 개수를 구하는 함수  
    cnt = 0
    for i in range(1,num+1):
        cnt = cnt+1 if num % i == 0 else cnt       
    return cnt

print(solution(13,17))