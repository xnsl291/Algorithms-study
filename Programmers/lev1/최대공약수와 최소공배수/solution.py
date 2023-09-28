#solution 1 내장함수사용
import math
def solution(n, m):
    max = math.gcd(m,n)
    min = int((m*n) / max)
    return max,min
  
