import sys

def solution(n):

    for i in range(n):
        result = i
        for length in range(len(str(i))):
            result+=int(str(i)[length])
        if result == n:
            return i
    return 0
        
print(solution(int(sys.stdin.readline())))