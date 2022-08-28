def solution(arr):
    arr.remove(sorted(arr)[0])
    return arr if len(arr)>0 else -1

#more simple
def solution2(arr):
    return [i for i in arr if i>min(arr)]