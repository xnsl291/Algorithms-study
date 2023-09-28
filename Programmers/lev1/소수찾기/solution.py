# # def solution(n):
# #     cnt = 0
# #     for i in range(1,n+1):
# #         if len([j for j in range(1,i+1) if i % j ==0]) == 2:
# #             cnt+=1
# #     return cnt

# # def solution(n):
# #     # find prime
# #     lst = [2,3,5,7]
# #     cnt = 0
    
# #     # 11^2 >120 이므로 11보다 작은수의 소수만 구해서 나누면 된다
# #     # 이면...
# #     # sqrt(n) 해서 
# #     for i in range(11,n):
# #         for j in lst:
# #             if i%j != 0 :
# #                 cnt+=1
# #         if cnt == len(lst):
# #             lst.append(i)
    
# #     if n<10:
# #         return len([i for i in lst if i<n])
# #     else:
# #         return (len(lst))
# # print(solution(100))

# def solution(n):
#     # n = 1610000
#     prime_lst=[]

#     for i in range(2,num+1):
#         #2-12
#         cnt = 0
        
#         print(f"i: {i}")
#         # prime_lst = [j for j in range(2,i+1) if i % j == 0]
        
#         for j in range(i,num):
#             print(f"j: {j}")
#             # if i =2
#             # j = 3,4,5,6,7,8,9,10,11,12,13
#             if i%j == 0:
#                 print(f"same i,j =  {i}, {j}")
#                 cnt +=1
#                 print(f"cnt = {cnt}")
                
#             print(f">>>>>>>>>>>>>>>>>>j = {j}")
            
#         if cnt == 1:
#             prime_lst.append(i)
#             print(f"list = [ {prime_lst} ] ")
        
#     # return len(prime_lst)
#     return prime_lst
    
# print(solution(36))
        
from time import process_time_ns


def solution(n):
    num = int(n**0.5)
    # 100까지 구한다 하면 sqrt(100)인 10까지의 소수를 구해서.... -> ?
    # 
    #약수 구하는 공식과 비슷하게 할 수 있지않나 
    
    #num = 10
    # for i in range(2,num):
    #     prime_lst = [j for j in range(i,num) if i%j ==0 ]
    # if 10/ (2~10) 의 나머지가 0이 아닌 수
    for j in range(2,num) :
        prime_lst = [ i for i in range(j,num+1) if i%j ==0 ]
    return prime_lst

#def solution(n):
    # ans_list = [i for i in range(1,n+1) if n%i ==0 ] 
    
    # return sum(ans_list)



print(solution(100))