def solution(numbers, target):
    cnt = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    
    while queue:
        tmp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([tmp+numbers[idx], idx])
            queue.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                cnt += 1
    return cnt


## 다른사람풀이 -- 재귀함수 사용 

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])