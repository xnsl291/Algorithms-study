from collections import Counter

def solution(array):

    lst = Counter(array).values()
    
    if list(lst).count(max(lst) )>1:
        return -1
    else:
        return list(Counter(array).keys())[list(lst).index(max(lst))]


# 다른 사람 풀이,,, 
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1