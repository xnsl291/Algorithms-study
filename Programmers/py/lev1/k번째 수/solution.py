def solution(array, commands):
    result = []
    for i in commands:
        start,end,index = i
        result.append(list(sorted(array[start-1:end]))[index-1])
    return result

#1줄코드작성해보기
def solution2(array, commands):
    return [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands ] 
