s = input()

new_s = []
for i in s:
    new_s.append(ord(i)-97)

# 빈 리스트 
ans = ['-1' for i in range(26)]
for idx, i in enumerate(new_s):
    if ans[i] == '-1':
        ans[i] = str(idx)
print(" ".join(ans))

