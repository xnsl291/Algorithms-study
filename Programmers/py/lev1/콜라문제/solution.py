def solution(a, b, n):
    answer = 0
    while n >= a:
        cnt = n // a * b
        answer += cnt
        n = (n % a) + cnt
    return answer
