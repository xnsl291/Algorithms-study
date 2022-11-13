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

def solution2(n,m):
  return lcm(n,m), gcd(n,m)
  
#solution 3 labda, 재귀 함수 
def solution3 (m,n) :
    gcd_ = lambda a,b: b if a%b==0 else gcd(b,a%b)
    lcm_ = int((m*n)/gcd_(n,m))
    return gcd_(n,m),lcm
  
