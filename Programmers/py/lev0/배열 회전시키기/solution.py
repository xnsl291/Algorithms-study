def solution(numbers, direction):
    return [numbers[-1]]+numbers[:-1] if direction == "right" else numbers[1:]+[numbers[0]]
    
# 다른사람 풀이
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)