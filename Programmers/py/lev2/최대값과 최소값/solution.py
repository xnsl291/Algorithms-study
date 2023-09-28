def solution(s):
    ans = [int(i) for i in s.split(" ")]
    return f'{min(ans)} {max(ans)}'

# s = "1 -2 3 4"
# print(solution(s))