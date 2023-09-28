import numpy as np
# solution1
def solution(array):
    return np.median(array)

# solution2
def solution(array):
    return sorted(array)[int(len(array)/2)]