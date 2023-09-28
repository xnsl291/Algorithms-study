#solution1
def solution1(n):
    text1 = "수박"
    
    ans = text1* int(n/2)

    if n%2 != 0:
        ans = ans+text1[:n%2]

    return ans
  
#solution 2
def solution2(n):
  return "수박" * (n//2) + "수"*(n%2)
  
#solution 3
def solution3(n):
  text = "수박" * round(n/2) 
  return text[:n]


  
