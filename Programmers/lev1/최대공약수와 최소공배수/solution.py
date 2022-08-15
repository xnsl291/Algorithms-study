#solution 1 내장함수사용
import math
def solution(n, m):
    max = math.gcd(m,n)
    min = int((m*n) / max)
    return max,min
    
#solution 2 재귀함수 
def gcd(n,,m):
  return m if a%b ==0 else gcd(b,a%b)

def lcm(n,m):
  return int((n*m)/gcd(n,m))

def solution(n,m):
  return lcm(n,m), gcd(n,m)
  
