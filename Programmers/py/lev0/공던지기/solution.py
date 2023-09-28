def solution(numbers, k):
    if len(numbers) < k*2:
        numbers = numbers * ((k*2) // len(numbers) + 1)
    return numbers[2*(k-1)]

# 다른사람 풀이
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]