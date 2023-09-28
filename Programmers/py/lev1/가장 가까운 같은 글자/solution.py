def solution(s):
    arr = []
    answer = []
    for idx  , value in enumerate(s):
        if value not in arr:
            answer.append(-1)
        else:
            answer.append(abs(arr.index(value) - idx))
            arr[arr.index(value)] = 0
            
        arr.append(value)
    return answer
