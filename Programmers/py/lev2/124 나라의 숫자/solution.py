# 모든 수를 1,2,4로만 사용해 표현

def solution(n):
    result = str(n//3-1 if n%3 ==0 else n//3 )+ str(4 if n%3==0 else n%3) 
    return int(result.replace('3','4'))
