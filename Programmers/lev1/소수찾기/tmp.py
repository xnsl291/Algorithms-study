# import numpy as np

# print(np.sqrt(124))


# print(np.sqrt(161)) #12.68  -> 13^2 보다 작으니까 12까지만 구하면 됨 
# np.sqrt(1)

# int(161**0.5) #이거까지만 구하면 되겠네 


# 소수리스트 따로 만들기? 
n = 100
prime_lst=[]
num = int(n**0.5)+1
print(num)
for i in range(2,num+1):
    #2-12
    cnt = 0
    # prime_lst = [j for j in range(2,i+1) if i % j == 0]
    
    for j in range(1,i+1):
        # if i =2
        # j = 3,4,5,6,7,8,9,10,11,12,13
        if i%j ==0:
            cnt +=1
    if cnt == 2:
        prime_lst.append(i)
    
print(prime_lst)
print(str(n**0.5).split(".")[0])