# solution1
def solution(price, money, count):
    remain = money - sum([price * i for i in range(1,count+1)])
    return 0 if remain>0 else remain*-1

# solution2
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
print(solution(3,20,4))