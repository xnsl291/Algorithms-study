from itertools import combinations

lst = [int(input()) for _ in range(9)]

for combi in list(combinations(lst, 7)):
    if sum(combi) == 100 :
        result = sorted(combi)
        break
    
for i in result:
    print(i)


