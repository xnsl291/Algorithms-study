def solution(arr, divisor):
    arr= sorted([ i for i in arr if i%divisor ==0 ])
    return [-1] if len(arr) <1 else arr

#or 사용
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
# 앞의 값이 참일경우 or 앞에만, 거짓일 경우 뒤에것까지 호출