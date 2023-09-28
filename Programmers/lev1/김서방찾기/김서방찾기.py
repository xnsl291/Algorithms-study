#solution 1 
def solution(seoul):
    for i in range(len(seoul)):
        if "kim" in seoul:
            idx = i
    ans = (f"김서방은 {idx}에 있다")
    return ans

#solution 2 -> clean ver.
def solution2(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다")
