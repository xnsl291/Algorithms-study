#solution 1
def solution(s):
    #테스트 케이스에 대문자만 카운트 하는 케이스도 있는지 
    #이 기능 쓰니까 몇몇 케이스에서 오류났었음
    # s.lower()
    
    p = s.count("p") + s.count("P")
    y = s.count("y") + s.count("Y")

    if p!=y:
        return False
    return True
    
 
#solution 2
#1줄로 간결하게 표현하기
def solution(s):
   return False if (s.count("p") + s.count("P")) != (s.count("y") + s.count("Y")) else True

