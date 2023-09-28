def solution(n):
    cnt = 1
    while (6 * answer % n):
        cnt += 1
    return cnt

##################################
# math 내장함수도 있음 
# gcd:최대공약수 , lcm :최소공배수
##################################
# import math
# def solution(n):
#     print(math.gcd(n, 6))
#     return (n * 6) // (math.gcd(n, 6)* 6)
