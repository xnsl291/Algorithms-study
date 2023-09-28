def solution(arr):
    tmp = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            tmp.append(arr[i])
    tmp.append(arr[-1])
    return tmp