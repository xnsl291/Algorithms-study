

######################
# N = int(input())  # 2
# lst = input().split(" ")  # 5 6
# add,sub,mul,div = input().split(" ")  # 2 1 1 1


################
### FOR CONVINENCE 
N =  2
tmp_num_lst = '5 6'
num_lst = [int(i) for i in tmp_num_lst.split(" ")]

tmp_input = '2 1 1 1'
tmp = tmp_input.split(" ")


if N >1 and N < 12 :
    pass  
# total 60 combination is possible 

from itertools import permutations

# 연산자들의 리스트를 따로 생성해야하나...? 
# add, sub, mul, div

cal_lst = []
# for i in range(len(tmp)):
#     for j in range(int(tmp[i])):
#         if i == 0:
#             cal_lst.append("+")
#         elif i == 1:
#             cal_lst.append("-")
#         elif i == 2:
#             cal_lst.append("*")
#         else:
#             cal_lst.append("/")
cal_lst = []
for index, i in enumerate(tmp):
    [cal_lst.append(str(index)) for i in range(int(tmp[index]))]
# bfs로 중복순열 구현가능 

print(cal_lst)
# 0 = add , 1 = sub, 2 = mul , 3 = div 

# 중복이 있는 순열로 중복제거 해줘야함 
# 현재 60개 출력해야 하는데 120개 출력중 


# 연산자들의 조합을 찾은 다음에 
tmp_lst = list(permutations(cal_lst,len(cal_lst)))
# dup_lst = []
# for i in range(len(tmp_lst)):
#     for j in range(1,len(tmp_lst)-i):
#         if tmp_lst[j+i] == tmp_lst[i]:
#             dup_lst.append(tmp_lst[i])
# sol1 - for loop
new_lst = []
# for v in tmp_lst:
#     if v not in new_lst:
#         new_lst.append(v)
# [new_lst.append(v) for v in tmp_lst if v not in new_lst ]

# sol2 - set
# new_lst = list(set(tmp_lst))

# sol3 - dict
new_lst = list(dict.fromkeys(tmp_lst)) #리스트 값들을 키로 변경

# print(len(tmp_lst))
# print(len(dup_lst))
print(new_lst)  
# 앞에서부터 차례로 계산 

# 최댓값과 최소값 저장 후 출력 

# ss = ["+","//","*"]
# nn = [1,2,3]
# for i in nn:
#     for j in ss:
#         if j == "+":

# print(type(add))
