def solution(arr, divisor):
    arr= sorted([ i for i in arr if i%divisor ==0 ])
    return [-1] if len(arr) <1 else arr