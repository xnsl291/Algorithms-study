import itertools

def solution(number):
    lst = itertools.combinations(number,3)
    return sum([ 1 for i in lst if sum(i)==0 ]) 
    
# num = [-2, 3, 0, 2, -5]  #2
# num = [-3, -2, -1, 0, 1, 2, 3]  #5
num = [-1, 1, -1, 1]  # 0

print(solution(num))