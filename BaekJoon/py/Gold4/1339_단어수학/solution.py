import sys 

num = int(sys.stdin.readline())

alpha_dict = {chr(65+i):0 for i in range(26)}
lst = [] 
for _ in range(num):
    target=sys.stdin.readline()[:-1].upper()
    lst.append(target)
    for j in range(len(target)):
        alpha_dict[target[-1-j]] += (10**j)
        
sorted_dict = sorted(alpha_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    alpha_dict[sorted_dict[i][0]] = 9-i

answer = 0 
for i in lst:
    tmp = list(i)
    for j in range(len(i)):
        tmp[j] = str(alpha_dict[tmp[j]])
    print(int("".join(tmp)))
    answer += int("".join(tmp))
        
print(answer)




# 다른사람 풀이
# import sys
# input = sys.stdin.readline

# N = int(input())
# alpha = dict()

# for _ in range(N):
#     word = input().rstrip()
#     for i, ch in enumerate(word):
#         idx = len(word) - i
#         alpha[ch] = alpha.get(ch, 0) + 10**(idx-1)

# ans = 0
# for idx, v in enumerate(sorted(alpha.values(), reverse=True)):
#     now = (9-idx) * v
#     ans += now
# print(ans)