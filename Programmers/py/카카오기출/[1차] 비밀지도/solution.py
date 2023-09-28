def solution(n, arr1, arr2):
    return [f"% {n}s"%bin( arr1[i] | arr2[i])[2:].replace("1","#").replace("0"," ") for i in range(n) ]
