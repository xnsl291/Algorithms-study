# def solution(n):
#     for i in range(2,n):
#         if i%n == 1:
#             return i
    

def solution(n):
    for i in range(2,n):
        if ( n%i == 1):
            return i
ans = solution(12)
print(ans)
