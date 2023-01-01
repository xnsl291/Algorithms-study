import itertools

def solution(numbers):
    tmp = []
    tmp += itertools.combinations(numbers,2)

    answer = [ sum(tmp[i]) for i in range(len(tmp))]
    return sorted(set(answer))



# lst = [5,0,2,7]
# lst = [2,1,3,4,1]
# print(solution(lst))