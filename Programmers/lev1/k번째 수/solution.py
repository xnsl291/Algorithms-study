def solution(array, commands):
    result = []
    for i in commands:
        start,end,index = i
        result.append(list(sorted(array[start-1:end]))[index-1])
    return result
