def solution(n):
    return [int(i) for i in reversed(str(n))]
    # return list(map(int, reversed(str(n))))