import sys

n = int(sys.stdin.readline())
n_lst = set(sys.stdin.readline().split()[:n])

m = int(sys.stdin.readline())
m_lst = sys.stdin.readline().split()[:m]

for i in m_lst:
    print(1 if i in n_lst else 0)

