import sys
from itertools import combinations

n,m = list(map(int,sys.stdin.readline().split()))
cardNum = list(map(int,sys.stdin.readline().split()))[:n]

sub_lst = sorted([(abs(m-i),i) for i in cardNum])
combi_lst = list(combinations(sub_lst, 3))
answer = sorted([combi_lst[i][0][1]+combi_lst[i][1][1]+combi_lst[i][2][1] for i in range(len(combi_lst)) if (combi_lst[i][0][1]+combi_lst[i][1][1]+combi_lst[i][2][1] )<=m  ])[-1]

print(answer)
