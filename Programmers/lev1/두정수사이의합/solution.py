#solution 1 
def solution1(a, b):
    answer = 0
    
    if a<b:
        ans_list = list(range(a,b+1))
    else:
        ans_list = list(range(b,a+1))
        
    return sum(ans_list)


#solution2
def solution2(a,b):
  if a>b: 
    a,b = b,a #a와b값 서로 교환 
  return sum(range(a,b+1))


#solution3
#가우스 법칙 - (n * n+1)/2
def solution3(a,b):
  return (abs(a-b)+1)*(a+b)//2
